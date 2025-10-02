"""Model252 module."""

from dataclasses import dataclass, field
from typing import ClassVar

import numpy as np
import pandas as pd
from numpy.typing import NDArray

from ..hlm import ModelForcings, ModelParameters, ModelStates, NodeParameters
from ..hlm_bmi import BmiFields, HlmBmi

DAYS_IN_MONTH = 30
SECONDS_IN_HOUR = 3600.0
SECONDS_IN_DAY = 86400.0
MILLIMETER_IN_METER = 1000.0

S_R = 1.0  # m. Ref val


@dataclass
class Model252NodeParameters(NodeParameters):
    """Model252 node parameters."""

    a_i: float
    l_i: float
    a_h: float
    invtau: float
    k_2: float
    k_i: float


@dataclass
class Model252States(ModelStates):
    """Model252 states."""

    fields: ClassVar[tuple] = ("q", "s_p", "s_t", "s_s")

    q: float = 1.0e-6  # Channel discharge [m**3 s**-1]
    s_p: float = 0.0  # Water ponded on hillslope surface [m]
    s_t: float = 0.0  # Effective water depth in the top soil layer [m]
    s_s: float = 0.0  # Effective water depth in hillslope subsurface [m]


@dataclass
class Model252Parameters(
    ModelParameters
):  # pylint:disable=too-many-instance-attributes
    """Model252 global parameters."""

    v_0: float = 0.33  # m s-1
    lambda_1: float = 0.2
    lambda_2: float = -0.1
    v_h: float = 0.02  # m s-1
    k_3: float = 2.0425e-6 / 60.0  # s-1
    k_i_factor: float = 0.02
    h_b: float = 0.5  # m
    s_l: float = 0.1  # m
    a: float = 0.0
    b: float = 99.0
    exponent: float = 3.0
    v_b: float = 0.75  # m s-1


def create_model252_bmi_fields():
    return BmiFields(
        component_name="HLM#252",
        input_var_names=(
            "atmosphere_water__precipitation_leq-volume_flux",
            "land_surface_water__potential_evaporation_volume_flux",
        ),
        input_var_units=(
            "m s-1",
            "m s-1",
        ),
        output_var_names=(
            "channel_discharge",
            "water_ponded_on_hillslope_surface",
            "effective_water_depth_in_the_top_soil_layer",
            "effective_water_depth_in_hillslope_subsurface",
        ),
        output_var_units=(
            "m3 s-1",
            "m",
            "m",
            "m",
        ),
    )


@dataclass
class Model252Forcings(ModelForcings):
    """Model252 forcings."""

    precipitation: pd.DataFrame = field(default_factory=pd.DataFrame)
    potential_evaporation: pd.DataFrame = field(default_factory=pd.DataFrame)


@dataclass
class EvaporationFluxes:
    """Evaporation fluxes dataclass."""

    e_p: float
    e_t: float
    e_s: float


@dataclass
class StorageFluxes:
    """Storage fluxes dataclass."""

    q_pl: float
    q_pt: float
    q_ts: float
    q_sl: float


@dataclass
class Model252(HlmBmi[Model252Parameters, Model252Forcings, Model252States]):
    """Model252 class."""

    parameters: Model252Parameters = field(default_factory=Model252Parameters)
    forcings_data: Model252Forcings = field(default_factory=Model252Forcings)
    initial_values: Model252States = field(default_factory=Model252States)

    bmi_fields: BmiFields = field(default_factory=create_model252_bmi_fields)

    def equations(
        self,
        t: float,
        y: NDArray[np.float64],
        node_id: int,
        # dense_output: bool,
    ) -> NDArray[np.float64]:
        """Compute the updated derivatives using dense solutions."""

        node_param: Model252NodeParameters = self.network.nodes[node_id]["parameters"]
        states = Model252States.from_array(y)
        children_solutions = self.get_children_solutions(node_id, t)

        precipitation = self.get_input(self.forcings_data.precipitation, node_id, t)
        evaporation_fluxes = self.get_evaporation_fluxes(t, node_id, states)
        storage_fluxes = self.get_storage_fluxes(states, node_param)

        discharge = self.get_discharge(
            states,
            node_param,
            storage_fluxes,
            children_solutions,
        )

        ponded = (
            precipitation
            - storage_fluxes.q_pl
            - storage_fluxes.q_pt
            - evaporation_fluxes.e_p
        )
        topsoil = storage_fluxes.q_pt - storage_fluxes.q_ts - evaporation_fluxes.e_t
        subsurface = storage_fluxes.q_ts - storage_fluxes.q_sl - evaporation_fluxes.e_s

        return np.array(
            [
                discharge,
                ponded,
                topsoil,
                subsurface,
            ]
        )

    def get_evaporation_fluxes(
        self,
        t: float,
        node_id: int,
        states: Model252States,
    ) -> EvaporationFluxes:
        """Get evaporation fluxes."""

        model_param = self.parameters

        potential_evaporation = self.get_input(
            self.forcings_data.potential_evaporation, node_id, t
        )

        if potential_evaporation <= 0.0:
            return EvaporationFluxes(0.0, 0.0, 0.0)

        corr = (
            states.s_p
            + states.s_t / model_param.s_l
            + states.s_s / (model_param.h_b - model_param.s_l)
        )
        if corr <= 1e-12:
            return EvaporationFluxes(0.0, 0.0, 0.0)

        e_p = (states.s_p / S_R) * potential_evaporation / corr
        e_t = states.s_t / model_param.s_l * potential_evaporation / corr
        e_s = (
            states.s_s
            / (model_param.h_b - model_param.s_l)
            * potential_evaporation
            / corr
        )
        return EvaporationFluxes(e_p, e_t, e_s)

    def get_storage_fluxes(
        self,
        states: Model252States,
        node_param: Model252NodeParameters,
    ) -> StorageFluxes:
        """Get fluxes between storages."""

        model_param = self.parameters

        pow_term = (
            np.power(1.0 - states.s_t / model_param.s_l, model_param.exponent)
            if (1.0 - states.s_t / model_param.s_l > 0.0)
            else 0.0
        )
        k_t = node_param.k_2 * (model_param.a + model_param.b * pow_term)

        # Fluxes
        q_pl = node_param.k_2 * states.s_p  # q_{pc} = k_2 * s_p # [m/s]
        q_pt = k_t * states.s_p  # q_{pt} = k_t * s_p # [m/s]
        q_ts = node_param.k_i * states.s_t  # q_{ts} = k_i * s_t # [m/s]
        q_sl = model_param.k_3 * states.s_s  # q_{sc} = k_3 * s_s # [m/s]

        return StorageFluxes(q_pl, q_pt, q_ts, q_sl)

    def get_discharge(
        self,
        states: Model252States,
        node_param: Model252NodeParameters,
        storage_fluxes: StorageFluxes,
        children_solutions: list[tuple[NDArray[np.float64], float]],
    ) -> float:
        """Get discharge."""

        model_param = self.parameters
        # Discharge
        discharge = -states.q + node_param.a_h * (  # m3/s
            storage_fluxes.q_pl + storage_fluxes.q_sl
        )  # m2*(m/s) == m3/s

        # children_solutions[child_id] = (child_ode_result, child_flow_partition)

        for child_states, child_flow_partition in children_solutions:
            child_states_arr = Model252States.from_array(child_states)
            discharge_child = child_states_arr.q * child_flow_partition

            if discharge_child < 0:
                discharge_child = 1e-6
            discharge += discharge_child

        if states.q < 0 and model_param.lambda_1 < 1:
            return 0.0

        return node_param.invtau * np.power(states.q, model_param.lambda_1) * discharge

    def _calculate_additional_network_parameters(self) -> None:
        for node_id in self.network.nodes:
            model_parameters = self.parameters
            node_parameters = self.network.nodes[node_id]["parameters"]

            a_i = node_parameters[0]
            l_i = node_parameters[1] * 1e3  # km -> m
            a_h = node_parameters[2] * 1e6  # km2 -> m2
            # models/definitions/ConvertParams

            # Compute extra local parameters
            invtau = (
                model_parameters.v_0
                * pow(a_i, model_parameters.lambda_2)
                / ((1.0 - model_parameters.lambda_1) * l_i)
            )  # [1/s]

            k_2 = model_parameters.v_h * l_i / a_h  # [1/s]

            k_i = k_2 * model_parameters.k_i_factor  # [1/s]

            self.network.nodes[node_id]["parameters"] = Model252NodeParameters(
                a_i, l_i, a_h, invtau, k_2, k_i
            )

    def _load_forcing_series(self) -> None:
        super()._load_forcing_series()
        # Convert from mm/hr to m/s
        self.forcings_data.precipitation /= SECONDS_IN_HOUR * MILLIMETER_IN_METER
        # Convert from mm/month to m/s
        self.forcings_data.potential_evaporation /= (
            DAYS_IN_MONTH * SECONDS_IN_DAY * MILLIMETER_IN_METER
        )
