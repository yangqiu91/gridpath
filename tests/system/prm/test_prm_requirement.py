#!/usr/bin/env python
# Copyright 2017 Blue Marble Analytics LLC. All rights reserved.

from collections import OrderedDict
from importlib import import_module
import os.path
import sys
import unittest

from tests.common_functions import create_abstract_model, \
    add_components_and_load_data

TEST_DATA_DIRECTORY = \
    os.path.join(os.path.dirname(__file__), "..", "..", "test_data")

# Import prerequisite modules
PREREQUISITE_MODULE_NAMES = ["temporal.operations.timepoints",
                             "temporal.operations.horizons",
                             "temporal.investment.periods",
                             "geography.prm_zones"]
NAME_OF_MODULE_BEING_TESTED = "system.prm.prm_requirement"
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


class TestCarbonCap(unittest.TestCase):
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
                              horizon="",
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
                                     horizon="",
                                     stage=""
                                     )

    def test_data_loaded_correctly(self):
        """
        Test components initialized with data as expected
        :return:
        """
        m, data = add_components_and_load_data(
            prereq_modules=IMPORTED_PREREQ_MODULES,
            module_to_test=MODULE_BEING_TESTED,
            test_data_dir=TEST_DATA_DIRECTORY,
            horizon="",
            stage=""
        )
        instance = m.create_instance(data)

        # Set: PRM_ZONE_PERIODS_WITH_REQUIREMENT
        expected_cc_zone_periods = sorted([
            ("PRM_Zone1", 2020), ("PRM_Zone1", 2030),
            ("PRM_Zone2", 2020), ("PRM_Zone2", 2030)
        ])
        actual_cc_zone_periods = sorted([
            (z, p) for (z, p)
            in instance.PRM_ZONE_PERIODS_WITH_REQUIREMENT
        ])
        self.assertListEqual(expected_cc_zone_periods,
                             actual_cc_zone_periods)

        # Param: prm_target_mmt
        expected_cc_target = OrderedDict(sorted({
            ("PRM_Zone1", 2020): 60, ("PRM_Zone1", 2030): 60,
            ("PRM_Zone2", 2020): 60, ("PRM_Zone2", 2030): 60}
                                                 .items()
                                                 )
                                          )
        actual_cc_target = OrderedDict(sorted({
            (z, p): instance.prm_requirement_mw[z, p]
            for (z, p) in instance.PRM_ZONE_PERIODS_WITH_REQUIREMENT}
                                               .items()
                                               )
                                        )
        self.assertDictEqual(expected_cc_target, actual_cc_target)


if __name__ == "__main__":
    unittest.main()