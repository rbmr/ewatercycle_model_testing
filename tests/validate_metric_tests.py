"""
module containing tests for the metric_tests test bank.
"""
# this is for a false positive because we use dynamic code
#pylint:disable=no-member

import unittest
from unittest import mock
from unittest.mock import Mock

import pandas as pd

from ewatercycle_model_testing import metric_tests
from ewatercycle_model_testing.test_suite import TestSuite


class TestMetricTests(unittest.TestCase):
    """
    class that contains tests for the metric_tests test bank.
    """

# Commented out because of gitlab eqatercycle problems. NEEDS TO BE CODE AGAIN WHEN PIPELINE IS FIXED.
#     def validate_nash_sutcliffe_wflow_efficiency_low_Rees(self):
#         model = RunModelUtil.getwflowmodel()
#         testSuite = TestSuite()
#         result = None
#         for test in testSuite.tests.values():
#             if test.name == "nash_sutcliffe_efficiency_Rees":
#                 result = test.start(model, "RiverRunoff")
#
#         self.assertFalse(result["passed"])
#         self.assertEqual(result["reason"], 'Nash-Sutcliffe efficiency is unsatisfactory. Nash Sutcliffe was '
#  '-3.228892345720805 , which is lower than 0.36')

    def test_validate_nash_sutcliffe_efficiency_error_rees(self):
        """
        tests if the nash_sutcliffe_efficiency gives an error when necessary
        """
        model = Mock()
        model.setup.return_value = None
        model.initialize.return_value = None
        test_suite = TestSuite()
        result = None
        for test in test_suite.tests.values():
            if test.name == "nash_sutcliffe_efficiency_rees":
                result = test.start(model, "RiverRunoff")

        self.assertFalse(result["passed"])
        self.assertEqual(result["reason"], "Error occurred, the model did not run correctly")

    @mock.patch("ewatercycle_model_testing.metric_tests.get_observation_data_rees")
    @mock.patch("ewatercycle_model_testing.metric_tests.get_output_rees")
    def test_validate_nash_sutcliffe_efficiency_very_good_rees(self, mockoutput, mockobservation):
        """
        tests if the nash_sutcliffe_efficiency is very good when necessary
        """
        mockoutput.return_value = [3, 2, 3, 2, 1]
        mockobservation.return_value = pd.DataFrame({"GRDC": [3, 2, 3, 2, 1]})
        model = Mock()
        model.setup.return_value = ("bla", "bla")
        model.initialize.return_value = None
        test_suite = TestSuite()
        result = None
        for test in test_suite.tests.values():
            if test.name == "nash_sutcliffe_efficiency_rees":
                result = test.start(model, "RiverRunoff")

        self.assertTrue(result["passed"])
        self.assertEqual(result["reason"], 'Nash-Sutcliffe efficiency is very good. Nash Sutcliffe was 1 , which is '
 'higher than 0.75')

    @mock.patch("ewatercycle_model_testing.metric_tests.get_observation_data_rees")
    @mock.patch("ewatercycle_model_testing.metric_tests.get_output_rees")
    def test_validate_nash_sutcliffe_efficiency_satisfactory_rees(self, mockoutput, mockobservation):
        """
        tests if the nash_sutcliffe_efficiency is satisfactory when necessary
        """
        mockoutput.return_value = [1, 2, 3, 2, 2]
        model = Mock()
        model.setup.return_value = ("bla", "bla")
        model.initialize.return_value = None
        test_suite = TestSuite()
        mockobservation.return_value = pd.DataFrame({"GRDC": [1, 2, 3, 2, 1]})
        result = None
        for test in test_suite.tests.values():
            if test.name == "nash_sutcliffe_efficiency_rees":
                result = test.start(model, "RiverRunoff")

        self.assertTrue(result["passed"])
        self.assertEqual(result["reason"], 'Nash-Sutcliffe efficiency is satisfactory. Nash Sutcliffe was '
 '0.6428571428571429 , which is higher than 0.36')

# Commented out because of gitlab eqatercycle problems. NEEDS TO BE CODE AGAIN WHEN PIPELINE IS FIXED.
#     def test_validate_kling_gupta_wflow_efficiency_low_Rees(self):
#         model = RunModelUtil.getwflowmodel()
#         testSuite = TestSuite()
#         result = None
#         for test in testSuite.tests.values():
#             if test.name == "kling_gupta_efficiency_Rees":
#                 result = test.start(model, "RiverRunoff")
#
#         self.assertFalse(result["passed"])
#         self.assertEqual(result["reason"], 'Kling-Gupta efficiency is unsatisfactory. Kling Gupta was '
#  '-0.8964966536631627 , which is lower than -0.41')

    def test_validate_kling_gupta_efficiency_error_rees(self):
        """
        tests if the kling_gupta_efficiency gives an error when necessary
        """
        model = Mock()
        model.setup.return_value = None
        model.initialize.return_value = None
        test_suite = TestSuite()
        result = None
        for test in test_suite.tests.values():
            if test.name == "kling_gupta_efficiency_rees":
                result = test.start(model, "RiverRunoff")

        self.assertFalse(result["passed"])
        self.assertEqual(result["reason"], "Error occurred, the model did not run correctly")

    @mock.patch("ewatercycle_model_testing.metric_tests.get_observation_data_rees")
    @mock.patch("ewatercycle_model_testing.metric_tests.get_output_rees")
    def test_validate_kling_gupta_efficiency_very_good_rees(self, mockoutput, mockobservation):
        """
        tests if the kling_gupta_efficiency is very good when necessary
        """
        mockoutput.return_value = [3, 2, 3, 2, 1]
        mockobservation.return_value = pd.DataFrame({"GRDC": [3, 2, 3, 2, 1]})
        model = Mock()
        model.setup.return_value = ("bla", "bla")
        model.initialize.return_value = None
        test_suite = TestSuite()
        result = None
        for test in test_suite.tests.values():
            if test.name == "kling_gupta_efficiency_rees":
                result = test.start(model, "RiverRunoff")

        self.assertTrue(result["passed"])
        self.assertEqual(result["reason"], 'Kling-Gupta efficiency is very good. Kling Gupta was 1.0 , which is higher '
 'than 0.75')

    @mock.patch("ewatercycle_model_testing.metric_tests.get_observation_data_rees")
    @mock.patch("ewatercycle_model_testing.metric_tests.get_output_rees")
    def test_validate_kling_gupta_efficiency_satisfactory_rees(self, mockoutput, mockobservation):
        """
        tests if the kling_gupta_efficiency is satisfactory when necessary
        """
        mockoutput.return_value = [1, 2, 3, 2, 2]
        model = Mock()
        model.setup.return_value = ("bla", "bla")
        model.initialize.return_value = None
        test_suite = TestSuite()
        mockobservation.return_value = pd.DataFrame({"GRDC": [1, 3, 3, 2, 1]})
        result = None
        for test in test_suite.tests.values():
            if test.name == "kling_gupta_efficiency_rees":
                result = test.start(model, "RiverRunoff")

        self.assertTrue(result["passed"])
        self.assertEqual(result["reason"], 'Kling-Gupta efficiency is satisfactory. Kling Gupta was 0.5857864376269049 , '
 'which is higher than -0.41')

# Commented out because of gitlab ewatercycle problems. NEEDS TO BE CODE AGAIN WHEN PIPELINE IS FIXED.

 #    def validate_nash_sutcliffe_wflow_efficiency_low_Lobith(self):
 #        model = RunModelUtil.getwflowmodel()
 #        testSuite = TestSuite()
 #        result = None
 #        for test in testSuite.tests.values():
 #            if test.name == "nash_sutcliffe_efficiency_Lobith":
 #                result = test.start(model, "RiverRunoff")
 #
 #        self.assertFalse(result["passed"])
 #        self.assertEqual(result["reason"], 'Nash-Sutcliffe efficiency is unsatisfactory. Nash Sutcliffe was '
 # '-2.820040220752988 , which is lower than 0.36')

    def test_validate_nash_sutcliffe_efficiency_error_lobith(self):
        """
        tests if the nash_sutcliffe_efficiency gives an error when necessary
        """
        model = Mock()
        model.setup.return_value = None
        model.initialize.return_value = None
        test_suite = TestSuite()
        result = None
        for test in test_suite.tests.values():
            if test.name == "nash_sutcliffe_efficiency_lobith":
                result = test.start(model, "RiverRunoff")

        self.assertFalse(result["passed"])
        self.assertEqual(result["reason"], "Error occurred, the model did not run correctly")

    @mock.patch("ewatercycle_model_testing.metric_tests.get_observation_data_lobith")
    @mock.patch("ewatercycle_model_testing.metric_tests.get_output_lobith")
    def test_validate_nash_sutcliffe_efficiency_very_good_lobith(self, mockoutput, mockobservation):
        """
        tests if the nash_sutcliffe_efficiency is very good when necessary
        """
        mockoutput.return_value = [3, 2, 3, 2, 1]
        mockobservation.return_value = pd.DataFrame({"GRDC": [3, 2, 3, 2, 1]})
        model = Mock()
        model.setup.return_value = ("bla", "bla")
        model.initialize.return_value = None
        test_suite = TestSuite()
        result = None
        for test in test_suite.tests.values():
            if test.name == "nash_sutcliffe_efficiency_lobith":
                result = test.start(model, "RiverRunoff")

        self.assertTrue(result["passed"])
        self.assertEqual(result["reason"], 'Nash-Sutcliffe efficiency is very good. Nash Sutcliffe was 1 , which is '
 'higher than 0.75')

    @mock.patch("ewatercycle_model_testing.metric_tests.get_observation_data_lobith")
    @mock.patch("ewatercycle_model_testing.metric_tests.get_output_lobith")
    def test_validate_nash_sutcliffe_efficiency_satisfactory_lobith(self, mockoutput, mockobservation):
        """
        tests if the nash_sutcliffe_efficiency is satisfactory when necessary
        """
        mockoutput.return_value = [1, 2, 3, 2, 2]
        model = Mock()
        model.setup.return_value = ("bla", "bla")
        model.initialize.return_value = None
        test_suite = TestSuite()
        mockobservation.return_value = pd.DataFrame({"GRDC": [1, 2, 3, 2, 1]})
        result = None
        for test in test_suite.tests.values():
            if test.name == "nash_sutcliffe_efficiency_lobith":
                result = test.start(model, "RiverRunoff")

        self.assertTrue(result["passed"])
        self.assertEqual(result["reason"], 'Nash-Sutcliffe efficiency is satisfactory. Nash Sutcliffe was '
 '0.6428571428571429 , which is higher than 0.36')

# Commented out because of gitlab eqatercycle problems. NEEDS TO BE CODE AGAIN WHEN PIPELINE IS FIXED.

 #    def test_validate_kling_gupta_wflow_efficiency_low_Lobith(self):
 #        model = RunModelUtil.getwflowmodel()
 #        testSuite = TestSuite()
 #        result = None
 #        for test in testSuite.tests.values():
 #            if test.name == "kling_gupta_efficiency_Lobith":
 #                result = test.start(model, "RiverRunoff")
 #
 #        self.assertFalse(result["passed"])
 #        self.assertEqual(result["reason"], 'Kling-Gupta efficiency is unsatisfactory. Kling Gupta was '
 # '-0.8972883450899871 , which is lower than -0.41')

    def test_validate_kling_gupta_efficiency_error_lobith(self):
        """
        tests if the kling_gupta_efficiency gives an error when necessary
        """
        model = Mock()
        model.setup.return_value = None
        model.initialize.return_value = None
        test_suite = TestSuite()
        result = None
        for test in test_suite.tests.values():
            if test.name == "kling_gupta_efficiency_lobith":
                result = test.start(model, "RiverRunoff")

        self.assertFalse(result["passed"])
        self.assertEqual(result["reason"], "Error occurred, the model did not run correctly")

    @mock.patch("ewatercycle_model_testing.metric_tests.get_observation_data_lobith")
    @mock.patch("ewatercycle_model_testing.metric_tests.get_output_lobith")
    def test_validate_kling_gupta_efficiency_very_good_lobith(self, mockoutput, mockobservation):
        """
        tests if the kling_gupta_efficiency is very good when necessary
        """
        mockoutput.return_value = [3, 2, 3, 2, 1]
        mockobservation.return_value = pd.DataFrame({"GRDC": [3, 2, 3, 2, 1]})
        model = Mock()
        model.setup.return_value = ("bla", "bla")
        model.initialize.return_value = None
        test_suite = TestSuite()
        result = None
        for test in test_suite.tests.values():
            if test.name == "kling_gupta_efficiency_lobith":
                result = test.start(model, "RiverRunoff")

        self.assertTrue(result["passed"])
        self.assertEqual(result["reason"], 'Kling-Gupta efficiency is very good. Kling Gupta was 1.0 , which is higher '
                                           'than 0.75')

    @mock.patch("ewatercycle_model_testing.metric_tests.get_observation_data_lobith")
    @mock.patch("ewatercycle_model_testing.metric_tests.get_output_lobith")
    def test_validate_kling_gupta_efficiency_satisfactory_lobith(self, mockoutput, mockobservation):
        """
        tests if the kling_gupta_efficiency is satisfactory when necessary
        """
        mockoutput.return_value = [1, 2, 3, 2, 2]
        model = Mock()
        model.setup.return_value = ("bla", "bla")
        model.initialize.return_value = None
        test_suite = TestSuite()
        mockobservation.return_value = pd.DataFrame({"GRDC": [1, 3, 3, 2, 1]})
        result = None
        for test in test_suite.tests.values():
            if test.name == "kling_gupta_efficiency_lobith":
                result = test.start(model, "RiverRunoff")

        self.assertTrue(result["passed"])
        self.assertEqual(result["reason"], 'Kling-Gupta efficiency is satisfactory. Kling Gupta was 0.5857864376269049 , '
                                           'which is higher than -0.41')


# Commented out because of gitlab ewatercycle problems. DOES WORK.

 #    def test_validate_nash_sutcliffe_wflow_efficiency_low_Schermbeck(self):
 #        model = RunModelUtil.getwflowmodel()
 #        testSuite = TestSuite()
 #        result = None
 #        for test in testSuite.tests.values():
 #            if test.name == "nash_sutcliffe_efficiency_schermbeck":
 #                result = test.start(model, "RiverRunoff")
 #
 #        self.assertFalse(result["passed"])
 #        self.assertEqual(result["reason"], 'Nash-Sutcliffe efficiency is unsatisfactory. Nash Sutcliffe was '
 # '-2.820040220752988 , which is lower than 0.36')

    def test_validate_nash_sutcliffe_efficiency_error_schermbeck(self):
        """
        tests if the nash_sutcliffe_efficiency gives an error when necessary
        """
        model = Mock()
        model.setup.return_value = None
        model.initialize.return_value = None
        test_suite = TestSuite()
        result = None
        for test in test_suite.tests.values():
            if test.name == "nash_sutcliffe_efficiency_schermbeck":
                result = test.start(model, "RiverRunoff")

        self.assertFalse(result["passed"])
        self.assertEqual(result["reason"], "Error occurred, the model did not run correctly")

    @mock.patch("ewatercycle_model_testing.metric_tests.get_observation_data_schermbeck")
    @mock.patch("ewatercycle_model_testing.metric_tests.get_output_schermbeck")
    def test_validate_nash_sutcliffe_efficiency_very_good_schermbeck(self, mockoutput, mockobservation):
        """
        tests if the nash_sutcliffe_efficiency is very good when necessary
        """
        mockoutput.return_value = [3, 2, 3, 2, 1]
        mockobservation.return_value = pd.DataFrame({"GRDC": [3, 2, 3, 2, 1]})
        model = Mock()
        model.setup.return_value = ("bla", "bla")
        model.initialize.return_value = None
        test_suite = TestSuite()
        result = None
        for test in test_suite.tests.values():
            if test.name == "nash_sutcliffe_efficiency_schermbeck":
                result = test.start(model, "RiverRunoff")

        self.assertTrue(result["passed"])
        self.assertEqual(result["reason"], 'Nash-Sutcliffe efficiency is very good. Nash Sutcliffe was 1 , which is '
 'higher than 0.75')

    @mock.patch("ewatercycle_model_testing.metric_tests.get_observation_data_schermbeck")
    @mock.patch("ewatercycle_model_testing.metric_tests.get_output_schermbeck")
    def test_validate_nash_sutcliffe_efficiency_satisfactory_schermbeck(self, mockoutput, mockobservation):
        """
        tests if the nash_sutcliffe_efficiency is satisfactory when necessary
        """
        mockoutput.return_value = [1, 2, 3, 2, 2]
        model = Mock()
        model.setup.return_value = ("bla", "bla")
        model.initialize.return_value = None
        test_suite = TestSuite()
        mockobservation.return_value = pd.DataFrame({"GRDC": [1, 2, 3, 2, 1]})
        result = None
        for test in test_suite.tests.values():
            if test.name == "nash_sutcliffe_efficiency_schermbeck":
                result = test.start(model, "RiverRunoff")

        self.assertTrue(result["passed"])
        self.assertEqual(result["reason"], 'Nash-Sutcliffe efficiency is satisfactory. Nash Sutcliffe was '
 '0.6428571428571429 , which is higher than 0.36')

# Commented out because of gitlab eqatercycle problems. NEEDS TO BE CODE AGAIN WHEN PIPELINE IS FIXED.

 #    def validate_kling_gupta_wflow_efficiency_low_schermbeck(self):
 #        model = RunModelUtil.getwflowmodel()
 #        testSuite = TestSuite()
 #        result = None
 #        for test in testSuite.tests.values():
 #            if test.name == "kling_gupta_efficiency_schermbeck":
 #                result = test.start(model, "RiverRunoff")
 #
 #        self.assertFalse(result["passed"])
 #        self.assertEqual(result["reason"], 'Kling-Gupta efficiency is unsatisfactory. Kling Gupta was '
 # '-0.8972883450899871 , which is lower than -0.41')

    def test_validate_kling_gupta_efficiency_error_schermbeck(self):
        """
        tests if the kling_gupta_efficiency gives an error when necessary
        """
        model = Mock()
        model.setup.return_value = None
        model.initialize.return_value = None
        test_suite = TestSuite()
        result = None
        for test in test_suite.tests.values():
            if test.name == "kling_gupta_efficiency_schermbeck":
                result = test.start(model, "RiverRunoff")

        self.assertFalse(result["passed"])
        self.assertEqual(result["reason"], "Error occurred, the model did not run correctly")

    @mock.patch("ewatercycle_model_testing.metric_tests.get_observation_data_schermbeck")
    @mock.patch("ewatercycle_model_testing.metric_tests.get_output_schermbeck")
    def test_validate_kling_gupta_efficiency_very_good_schermbeck(self, mockoutput, mockobservation):
        """
        tests if the kling_gupta_efficiency is very good when necessary
        """
        mockoutput.return_value = [3, 2, 3, 2, 1]
        mockobservation.return_value = pd.DataFrame({"GRDC": [3, 2, 3, 2, 1]})
        model = Mock()
        model.setup.return_value = ("bla", "bla")
        model.initialize.return_value = None
        test_suite = TestSuite()
        result = None
        for test in test_suite.tests.values():
            if test.name == "kling_gupta_efficiency_schermbeck":
                result = test.start(model, "RiverRunoff")

        self.assertTrue(result["passed"])
        self.assertEqual(result["reason"], 'Kling-Gupta efficiency is very good. Kling Gupta was 1.0 , which is higher '
                                           'than 0.75')

    @mock.patch("ewatercycle_model_testing.metric_tests.get_observation_data_schermbeck")
    @mock.patch("ewatercycle_model_testing.metric_tests.get_output_schermbeck")
    def test_validate_kling_gupta_efficiency_satisfactory_schermbeck(self, mockoutput, mockobservation):
        """
        tests if the kling_gupta_efficiency is satisfactory when necessary
        """
        mockoutput.return_value = [1, 2, 3, 2, 2]
        model = Mock()
        model.setup.return_value = ("bla", "bla")
        model.initialize.return_value = None
        test_suite = TestSuite()
        mockobservation.return_value = pd.DataFrame({"GRDC": [1, 3, 3, 2, 1]})
        result = None
        for test in test_suite.tests.values():
            if test.name == "kling_gupta_efficiency_schermbeck":
                result = test.start(model, "RiverRunoff")

        self.assertTrue(result["passed"])
        self.assertEqual(result["reason"], 'Kling-Gupta efficiency is satisfactory. Kling Gupta was 0.5857864376269049 , '
                                           'which is higher than -0.41')
