#!/usr/bin/env python
# Copyright 2017 Blue Marble Analytics LLC. All rights reserved.

from __future__ import absolute_import

from .reserve_aggregation import generic_add_model_components


def add_model_components(m, d, scenario_directory, subproblem, stage):
    """

    :param m:
    :param d:
    :return:
    """

    generic_add_model_components(
        m,
        d,
        "lf_reserves_up_zone",
        "LF_RESERVES_UP_ZONES",
        "LF_RESERVES_UP_PROJECTS",
        "Provide_LF_Reserves_Up_MW",
        "Total_LF_Reserves_Up_Provision_MW"
        )
