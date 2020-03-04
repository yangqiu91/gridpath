#!/usr/bin/env python
# Copyright 2019 Blue Marble Analytics LLC. All rights reserved.

"""

"""

import os.path
import pandas as pd


# TODO: use this in capacity and operational type project subset
#  determinations
def determine_project_subset(
        scenario_directory, subproblem, stage, column, type
):
    """
    :param scenario_directory:
    :param subproblem:
    :param stage:
    :param column:
    :param type:
    :return:

    """

    project_subset = list()

    dynamic_components = \
        pd.read_csv(
            os.path.join(scenario_directory, subproblem, stage, "inputs",
                         "projects.tab"),
            sep="\t", usecols=["project", column]
        )

    for row in zip(dynamic_components["project"],
                   dynamic_components[column]):
        if row[1] == type:
            project_subset.append(row[0])
        else:
            pass

    return project_subset


def check_if_linear_horizon_first_timepoint(mod, tmp, balancing_type):
    return tmp == mod.first_horizon_timepoint[
        balancing_type, mod.horizon[tmp, balancing_type]] \
            and mod.boundary[
               balancing_type, mod.horizon[tmp, balancing_type]] \
            == "linear"


def check_if_linear_horizon_last_timepoint(mod, tmp, balancing_type):
    return tmp == mod.last_horizon_timepoint[
        balancing_type, mod.horizon[tmp, balancing_type]] \
            and mod.boundary[
               balancing_type, mod.horizon[tmp, balancing_type]] \
            == "linear"
