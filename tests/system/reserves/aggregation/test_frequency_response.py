#!/usr/bin/env python
# Copyright 2017 Blue Marble Analytics LLC. All rights reserved.

from __future__ import print_function

from builtins import str
from collections import OrderedDict
from importlib import import_module
import os.path
import sys
import unittest

from tests.common_functions import create_abstract_model, \
    add_components_and_load_data

TEST_DATA_DIRECTORY = \
    os.path.join(os.path.dirname(__file__), "..", "..", "..", "test_data")

# Import prerequisite modules
PREREQUISITE_MODULE_NAMES = [
    "temporal.operations.timepoints", "temporal.operations.horizons",
    "temporal.investment.periods",
    "geography.load_zones",
    "geography.frequency_response_balancing_areas",
    "project", "project.capacity.capacity", "project.fuels",
    "project.operations",
    "project.operations.reserves.frequency_response",
    "system.reserves.requirement.frequency_response"
]
NAME_OF_MODULE_BEING_TESTED = "system.reserves.aggregation.frequency_response"
IMPORTED_PREREQ_MODULES = list()
for mdl in PREREQUISITE_MODULE_NAMES:
    try:
        imported_module = import_module("." + str(mdl), package="gridpath")
        IMPORTED_PREREQ_MODULES.append(imported_module)
    except ImportError:
        print("ERROR! Module " + str(mdl) + " not found.")
        sys.exit(1)
# Import the module we'll test
try:
    MODULE_BEING_TESTED = import_module("." + NAME_OF_MODULE_BEING_TESTED,
                                        package="gridpath")
except ImportError:
    print("ERROR! Couldn't import module " + NAME_OF_MODULE_BEING_TESTED +
          " to test.")


class TestFreqRespAgg(unittest.TestCase):
    """

    """
    def test_add_model_components(self):
        """
        Test that there are no errors when adding model components
        :return:
        """
        create_abstract_model(prereq_modules=IMPORTED_PREREQ_MODULES,
                              module_to_test=MODULE_BEING_TESTED,
                              test_data_dir=TEST_DATA_DIRECTORY,
                              subproblem="",
                              stage=""
                              )

    def test_load_model_data(self):
        """
        Test that data are loaded with no errors
        :return:
        """
        add_components_and_load_data(prereq_modules=IMPORTED_PREREQ_MODULES,
                                     module_to_test=MODULE_BEING_TESTED,
                                     test_data_dir=TEST_DATA_DIRECTORY,
                                     subproblem="",
                                     stage=""
                                     )

    def test_data_loaded_correctly(self):
        """
        Test components initialized with expected data
        :return:
        """
        m, data = add_components_and_load_data(
            prereq_modules=IMPORTED_PREREQ_MODULES,
            module_to_test=MODULE_BEING_TESTED,
            test_data_dir=TEST_DATA_DIRECTORY,
            subproblem="",
            stage=""
        )
        instance = m.create_instance(data)

        # Set: FREQUENCY_RESPONSE_PROJECTS_OPERATIONAL_IN_TIMEPOINT
        projects_2020 = sorted(["Gas_CCGT", "Gas_CCGT_New",
                                "Gas_CCGT_New_Binary", "Gas_CCGT_z2",
                                "Battery", "Battery_Specified", "Hydro",
                                "Hydro_NonCurtailable"])
        projects_2030 = sorted(["Gas_CCGT", "Gas_CCGT_New",
                                "Gas_CCGT_New_Binary", "Gas_CCGT_z2",
                                "Battery", "Hydro", "Hydro_NonCurtailable"])
        expected_projects = OrderedDict(sorted(
            {
                20200101: projects_2020,
                20200102: projects_2020,
                20200103: projects_2020,
                20200104: projects_2020,
                20200105: projects_2020,
                20200106: projects_2020,
                20200107: projects_2020,
                20200108: projects_2020,
                20200109: projects_2020,
                20200110: projects_2020,
                20200111: projects_2020,
                20200112: projects_2020,
                20200113: projects_2020,
                20200114: projects_2020,
                20200115: projects_2020,
                20200116: projects_2020,
                20200117: projects_2020,
                20200118: projects_2020,
                20200119: projects_2020,
                20200120: projects_2020,
                20200121: projects_2020,
                20200122: projects_2020,
                20200123: projects_2020,
                20200124: projects_2020,
                20200201: projects_2020,
                20200202: projects_2020,
                20200203: projects_2020,
                20200204: projects_2020,
                20200205: projects_2020,
                20200206: projects_2020,
                20200207: projects_2020,
                20200208: projects_2020,
                20200209: projects_2020,
                20200210: projects_2020,
                20200211: projects_2020,
                20200212: projects_2020,
                20200213: projects_2020,
                20200214: projects_2020,
                20200215: projects_2020,
                20200216: projects_2020,
                20200217: projects_2020,
                20200218: projects_2020,
                20200219: projects_2020,
                20200220: projects_2020,
                20200221: projects_2020,
                20200222: projects_2020,
                20200223: projects_2020,
                20200224: projects_2020,
                20300101: projects_2030,
                20300102: projects_2030,
                20300103: projects_2030,
                20300104: projects_2030,
                20300105: projects_2030,
                20300106: projects_2030,
                20300107: projects_2030,
                20300108: projects_2030,
                20300109: projects_2030,
                20300110: projects_2030,
                20300111: projects_2030,
                20300112: projects_2030,
                20300113: projects_2030,
                20300114: projects_2030,
                20300115: projects_2030,
                20300116: projects_2030,
                20300117: projects_2030,
                20300118: projects_2030,
                20300119: projects_2030,
                20300120: projects_2030,
                20300121: projects_2030,
                20300122: projects_2030,
                20300123: projects_2030,
                20300124: projects_2030,
                20300201: projects_2030,
                20300202: projects_2030,
                20300203: projects_2030,
                20300204: projects_2030,
                20300205: projects_2030,
                20300206: projects_2030,
                20300207: projects_2030,
                20300208: projects_2030,
                20300209: projects_2030,
                20300210: projects_2030,
                20300211: projects_2030,
                20300212: projects_2030,
                20300213: projects_2030,
                20300214: projects_2030,
                20300215: projects_2030,
                20300216: projects_2030,
                20300217: projects_2030,
                20300218: projects_2030,
                20300219: projects_2030,
                20300220: projects_2030,
                20300221: projects_2030,
                20300222: projects_2030,
                20300223: projects_2030,
                20300224: projects_2030
                                               }.items()
                                               )
                                        )
        actual_projects = OrderedDict(sorted(
            {tmp: sorted(
                [prj for prj in
                 instance.FREQUENCY_RESPONSE_PROJECTS_OPERATIONAL_IN_TIMEPOINT[tmp]
                 ]) for tmp in instance.TIMEPOINTS
                                                 }.items()
                                             )
                                      )
        self.assertDictEqual(expected_projects, actual_projects)

        # Set: FREQUENCY_RESPONSE_PARTIAL_PROJECTS_OPERATIONAL_IN_TIMEPOINT
        pprojects_2020 = sorted(["Gas_CCGT", "Gas_CCGT_New",
                                 "Gas_CCGT_New_Binary", "Gas_CCGT_z2"])
        pprojects_2030 = sorted(["Gas_CCGT", "Gas_CCGT_New",
                                 "Gas_CCGT_New_Binary", "Gas_CCGT_z2"])
        expected_pprojects = OrderedDict(sorted(
            {
                20200101: pprojects_2020,
                20200102: pprojects_2020,
                20200103: pprojects_2020,
                20200104: pprojects_2020,
                20200105: pprojects_2020,
                20200106: pprojects_2020,
                20200107: pprojects_2020,
                20200108: pprojects_2020,
                20200109: pprojects_2020,
                20200110: pprojects_2020,
                20200111: pprojects_2020,
                20200112: pprojects_2020,
                20200113: pprojects_2020,
                20200114: pprojects_2020,
                20200115: pprojects_2020,
                20200116: pprojects_2020,
                20200117: pprojects_2020,
                20200118: pprojects_2020,
                20200119: pprojects_2020,
                20200120: pprojects_2020,
                20200121: pprojects_2020,
                20200122: pprojects_2020,
                20200123: pprojects_2020,
                20200124: pprojects_2020,
                20200201: pprojects_2020,
                20200202: pprojects_2020,
                20200203: pprojects_2020,
                20200204: pprojects_2020,
                20200205: pprojects_2020,
                20200206: pprojects_2020,
                20200207: pprojects_2020,
                20200208: pprojects_2020,
                20200209: pprojects_2020,
                20200210: pprojects_2020,
                20200211: pprojects_2020,
                20200212: pprojects_2020,
                20200213: pprojects_2020,
                20200214: pprojects_2020,
                20200215: pprojects_2020,
                20200216: pprojects_2020,
                20200217: pprojects_2020,
                20200218: pprojects_2020,
                20200219: pprojects_2020,
                20200220: pprojects_2020,
                20200221: pprojects_2020,
                20200222: pprojects_2020,
                20200223: pprojects_2020,
                20200224: pprojects_2020,
                20300101: pprojects_2030,
                20300102: pprojects_2030,
                20300103: pprojects_2030,
                20300104: pprojects_2030,
                20300105: pprojects_2030,
                20300106: pprojects_2030,
                20300107: pprojects_2030,
                20300108: pprojects_2030,
                20300109: pprojects_2030,
                20300110: pprojects_2030,
                20300111: pprojects_2030,
                20300112: pprojects_2030,
                20300113: pprojects_2030,
                20300114: pprojects_2030,
                20300115: pprojects_2030,
                20300116: pprojects_2030,
                20300117: pprojects_2030,
                20300118: pprojects_2030,
                20300119: pprojects_2030,
                20300120: pprojects_2030,
                20300121: pprojects_2030,
                20300122: pprojects_2030,
                20300123: pprojects_2030,
                20300124: pprojects_2030,
                20300201: pprojects_2030,
                20300202: pprojects_2030,
                20300203: pprojects_2030,
                20300204: pprojects_2030,
                20300205: pprojects_2030,
                20300206: pprojects_2030,
                20300207: pprojects_2030,
                20300208: pprojects_2030,
                20300209: pprojects_2030,
                20300210: pprojects_2030,
                20300211: pprojects_2030,
                20300212: pprojects_2030,
                20300213: pprojects_2030,
                20300214: pprojects_2030,
                20300215: pprojects_2030,
                20300216: pprojects_2030,
                20300217: pprojects_2030,
                20300218: pprojects_2030,
                20300219: pprojects_2030,
                20300220: pprojects_2030,
                20300221: pprojects_2030,
                20300222: pprojects_2030,
                20300223: pprojects_2030,
                20300224: pprojects_2030
            }.items()
        )
        )
        actual_pprojects = OrderedDict(sorted(
            {tmp: sorted(
                [prj for prj in
                 instance.
                 FREQUENCY_RESPONSE_PARTIAL_PROJECTS_OPERATIONAL_IN_TIMEPOINT[
                     tmp]
                 ]) for tmp in instance.TIMEPOINTS
            }.items()
        )
        )
        self.assertDictEqual(expected_pprojects, actual_pprojects)

if __name__ == "__main__":
    unittest.main()
