#!/usr/bin/env python
# Copyright 2016-2020 Blue Marble Analytics LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pyomo.environ import Param, NonNegativeReals

from gridpath.system.reserves.requirement.reserve_requirements import \
    generic_get_inputs_from_database, generic_add_model_components, \
    generic_write_model_inputs, generic_load_model_data


def add_model_components(m, d, scenario_directory, subproblem, stage):
    """

    :param m:
    :param d:
    :return:
    """

    generic_add_model_components(
        m=m,
        d=d,
        reserve_zone_set="FREQUENCY_RESPONSE_BAS",
        reserve_requirement_tmp_param="frequency_response_requirement_mw",
        reserve_requirement_percent_param="fr_per_req",
        reserve_zone_load_zone_set="FR_BA_LZ",
        reserve_requirement_expression="Frequency_Response_Requirement"
        )

    # Also add the partial requirement for frequency response that can be
    # met by only a subset of the projects that can provide frequency response

    m.frequency_response_requirement_partial_mw = Param(
        m.FREQUENCY_RESPONSE_BAS, m.TMPS,
        within=NonNegativeReals,
        default=0
    )


def load_model_data(m, d, data_portal, scenario_directory, subproblem, stage):
    """
    
    :param m: 
    :param d: 
    :param data_portal: 
    :param scenario_directory: 
    :param stage:
    :param stage: 
    :return: 
    """
    generic_load_model_data(
        m=m, d=d, data_portal=data_portal,
        scenario_directory=scenario_directory, subproblem=subproblem,
        stage=stage,
        reserve_requirement_param="frequency_response_requirement_mw",
        reserve_zone_load_zone_set="FR_BA_LZ",
        reserve_requirement_percent_param="fr_per_req",
        reserve_type="frequency_response"
    )


def get_inputs_from_database(scenario_id, subscenarios, subproblem, stage, conn):
    """
    :param subscenarios: SubScenarios object with all subscenario info
    :param subproblem:
    :param stage:
    :param conn: database connection
    :return:
    """
    return \
        generic_get_inputs_from_database(
            scenario_id=scenario_id,
        subscenarios=subscenarios,
            subproblem=subproblem, stage=stage, conn=conn,
            reserve_type="frequency_response",
            reserve_type_ba_subscenario_id
            =subscenarios.FREQUENCY_RESPONSE_BA_SCENARIO_ID,
            reserve_type_req_subscenario_id
            =subscenarios.FREQUENCY_RESPONSE_SCENARIO_ID
        )


def validate_inputs(scenario_id, subscenarios, subproblem, stage, conn):
    """
    Get inputs from database and validate the inputs
    :param subscenarios: SubScenarios object with all subscenario info
    :param subproblem:
    :param stage:
    :param conn: database connection
    :return:
    """
    pass
    # Validation to be added
    # frequency_response = get_inputs_from_database(
    #     scenario_id, subscenarios, subproblem, stage, conn)


def write_model_inputs(scenario_directory, scenario_id, subscenarios, subproblem, stage, conn):
    """
    Get inputs from database and write out the model input
    frequency_response_requirement.tab file.
    :param scenario_directory: string, the scenario directory
    :param subscenarios: SubScenarios object with all subscenario info
    :param subproblem:
    :param stage:
    :param conn: database connection
    :return:
    """

    tmp_req, percent_req, percent_map = \
        get_inputs_from_database(scenario_id, subscenarios, subproblem, stage, conn)

    generic_write_model_inputs(
        scenario_directory=scenario_directory,
        subproblem=subproblem, stage=stage,
        timepoint_req=tmp_req,
        percent_req=percent_req, percent_map=percent_map,
        reserve_type="frequency_response"
    )
