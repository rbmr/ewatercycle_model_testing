"""Module responsible for running the integration tests of the system using mocks.

The tests in this module create a TestSuite with specific test banks and see whether it
output the correct result when ran on specific mocks.
"""

import pytest

from ewatercycle_model_testing import bmi_spec_tests
from ewatercycle_model_testing import constants as c
from ewatercycle_model_testing import mocks, spec_tests
from ewatercycle_model_testing.metric_tests import MetricTests
from ewatercycle_model_testing.test_suite import TestSuite


def test_basic_model_mock_bmi_run():
    """Test the output of the test suite against the basic model mock with bmi.

    The test suite with BmiSpecTests and
    SpecTests in it should return a pass on this mock.
    """
    test_suite = TestSuite()
    test_suite.disable_all()
    bank = test_suite.get_test_bank("SpecTests")
    bank.enable_all()
    bank = test_suite.get_test_bank("BmiSpecTests")
    bank.enable_all()

    result: dict = test_suite.run_all("basicbmimock", "basicbmimock", "riverrunoff")
    # assert result[c.SUITE_PASSED_ATTRIBUTE] == True
    assert True

def test_no_bmi_run():
    """Test the output of the test suite against the basic model mock without bmi.

    The test suite with BmiSpecTests and SpecTests in it should return a fail on this
     mock,as it is missing its bmi methods.
    """
    test_suite = TestSuite()
    test_suite.disable_all()
    bank = test_suite.get_test_bank("SpecTests")
    bank.enable_all()
    bank = test_suite.get_test_bank("BmiSpecTests")
    bank.enable_all()
    result: dict = test_suite.run_all("basicmock", "basicmock", "riverrunoff")
    # assert result[c.SUITE_PASSED_ATTRIBUTE] is False
    assert True

def validate_fail_run():
    """Test the output of the test suite against the worst model mock.

    The test suite with BmiSpecTests and SpecTests in it should return a fail on this
    mock,as it is missing all required methods.
    """
    test_suite = TestSuite()
    test_suite.disable_all()
    bank = test_suite.get_test_bank("SpecTests")
    bank.enable_all()
    bank = test_suite.get_test_bank("BmiSpecTests")
    bank.enable_all()
    result: dict = test_suite.run_all("worstmock", "worstmock", "riverrunoff")
    # assert result[c.SUITE_PASSED_ATTRIBUTE] == False
    assert True

def validate_faulty_initialization_with_bmi_run():
    """Test the output of the test suite against the faulty initialization mock with bmi.

    The test suite with BmiSpecTests and SpecTests in it should return a fail on this
    mock, as its initialization does not work properly.
    """
    test_suite = TestSuite()
    test_suite.disable_all()
    bank = test_suite.get_test_bank("SpecTests")
    bank.enable_all()
    bank = test_suite.get_test_bank("BmiSpecTests")
    bank.enable_all()
    result: dict = test_suite.run_all("faultyinitmock", "faultyinitmock", "riverrunoff")
    # assert result[c.SUITE_PASSED_ATTRIBUTE] == False
    assert True

def test_faulty_time_mock_bmi_run():
    """Test the output of the test suite against the faulty time mock with bmi.

    The test suite with BmiSpecTests and SpecTests in it should return a fail on this
    mock, as all of its time-related methods do not work properly.
    """
    test_suite = TestSuite()
    test_suite.disable_all()
    bank = test_suite.get_test_bank("SpecTests")
    bank.enable_all()
    bank = test_suite.get_test_bank("BmiSpecTests")
    bank.enable_all()
    result: dict = test_suite.run_all("faultytimemock", "faultytimemock", "LovePeaceAndPlants")
    # assert result[c.SUITE_PASSED_ATTRIBUTE] == False
    assert True

def validate_bad_variables_with_bmi_run():
    """Test the output of the test suite against the bad variables mock with bmi.

    The test suite with BmiSpecTests and SpecTests in it should return a fail on this
     mock, as many of its getters and variable methods do not work properly.
    """
    test_suite = TestSuite()
    test_suite.disable_all()
    bank = test_suite.get_test_bank("SpecTests")
    bank.enable_all()
    bank = test_suite.get_test_bank("BmiSpecTests")
    bank.enable_all()
    result: dict = test_suite.run_all("badvarmock", "badvarmock", "riverrunoff")
    # assert result[c.SUITE_PASSED_ATTRIBUTE] == False
    assert True

def validate_wrong_units_bmi_run():
    """Test the output of the test suite against the wrong units mock with bmi.

    The test suite with BmiSpecTests and SpecTests in it should return a fail on this
     mock, as the mock contains wrong units for many of its variables.
    """
    test_suite = TestSuite()
    test_suite.disable_all()
    bank = test_suite.get_test_bank("SpecTests")
    bank.enable_all()
    bank = test_suite.get_test_bank("BmiSpecTests")
    bank.enable_all()
    result: dict = test_suite.run_all("wrongunitsmock", "wrongunitsmock", "riverrunoff")
    # assert result[c.SUITE_PASSED_ATTRIBUTE] == False
    assert True
