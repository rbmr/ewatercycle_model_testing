"""module containing tests for the bmi_spec_tests test bank."""
import pytest

from ewatercycle_model_testing import mocks
from ewatercycle_model_testing.bmi_spec_tests import BmiSpecTests
from ewatercycle_model_testing.test_result import TestResult


def fetch_test(test_name):
    """Fetch a test from the bmi_spec_tests test bank by its name.

    Args:
       test_name: the name of the test to fetch

    Returns:
        Test: the test with the given name from the test bank

    Raises:
        Exception: if a test with the given name does not exist in the test bank
    """
    for temp in BmiSpecTests.tests:
        if temp.name == test_name:
            return temp
    raise Exception("that test doesn't exist in the SpecTests bank!")


def validate_correct_start_time_condition_test():
    """Test the correct_start_time_condition test."""
    test = fetch_test("correct_start_time_condition")
    mock = mocks.BasicModelMockWithBmi()
    assert test.run(mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False,
                          "The bmi method get_start_time() throws an unexpected error!")
    mock = mocks.WrongUnitsBmiMock()
    assert test.run(mock,0) == TestResult(False,
                            "The bmi method get_start_time() does not return a number.")


def validate_correct_time_condition_test():
    """Test the correct_time_condition test."""
    test = fetch_test("correct_time_condition")
    mock = mocks.BasicModelMockWithBmi()
    assert test.run(mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False,
                        "The bmi method get_current_time() throws an unexpected error!")
    mock = mocks.WrongUnitsBmiMock()
    assert test.run(mock,0) == TestResult(False,
                          "The bmi method get_current_time() does not return a number.")


def validate_correct_end_time_condition_test():
    """Test the correct_end_time_condition test."""
    test = fetch_test("correct_end_time_condition")
    mock = mocks.BasicModelMockWithBmi()
    assert test.run(mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False,
                            "The bmi method get_end_time() throws an unexpected error!")
    mock = mocks.WrongUnitsBmiMock()
    assert test.run(mock,0) == TestResult(False,
                              "The bmi method get_end_time() does not return a number.")


def validate_finalize_model_condition_test():
    """Test the finalize_model_condition test."""
    test = fetch_test("finalize_model_condition")
    mock = mocks.BasicModelMockWithBmi()
    assert test.run(mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False,
                                "The bmi method finalize() throws an unexpected error!")


def validate_get_grid_x_condition_test():
    """Test the get_grid_x_condition test."""
    test = fetch_test("get_grid_x_condition")
    mock = mocks.BasicModelMockWithBmi()
    assert test.run(mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False,
                                  "The method get_grid_x() throws an unexpected error!")
    mock = mocks.BadVariablesMockWithBmi()
    assert test.run(mock,0) == TestResult(False,
             "The bmi method get_grid_x() returns a list with items other than numbers")


def validate_get_grid_y_condition_test():
    """Test the get_grid_y_condition test."""
    test = fetch_test("get_grid_y_condition")
    mock = mocks.BasicModelMockWithBmi()
    assert test.run(mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False,
                                  "The method get_grid_y() throws an unexpected error!")
    mock = mocks.BadVariablesMockWithBmi()
    assert test.run(mock,0) == TestResult(False,
             "The bmi method get_grid_y() returns a list with items other than numbers")


def validate_get_ouput_var_names_condition_test():
    """Test the get_ouput_var_names_condition test."""
    test = fetch_test("get_ouput_var_names_condition")
    mock = mocks.BasicModelMockWithBmi()
    assert test.run(mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False,
                     "The bmi method get_output_var_names() gives an unexpected error!")
    mock = mocks.BadVariablesMockWithBmi()
    assert test.run(mock,0) == TestResult(False,
                                      "The bmi method get_output_var_names()"
                                      " returns a list with items other than strings.")


def validate_get_time_step_condition_test():
    """Test the get_time_step_condition test."""
    test = fetch_test("get_time_step_condition")
    mock = mocks.BasicModelMockWithBmi()
    assert test.run(mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False,
                           "The bmi method get_time_step() throws an unexpected error!")
    mock = mocks.WrongUnitsBmiMock()
    assert test.run(mock,0) == TestResult(False,
                             "The bmi method get_time_step() does not return a number.")
    mock = mocks.FaultyTimeMockWithBmi()
    assert test.run(mock,0) == TestResult(False,
                      "The bmi method get_time_step() gives a time step of 0 or lower.")


def validate_grid_shape_condition_test():
    """Test the grid_shape_condition test."""
    test = fetch_test("grid_shape_condition")
    mock = mocks.BasicModelMockWithBmi()
    assert test.run(mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False,
                              "The method get_grid_shape() throws an unexpected error!")
    mock = mocks.BadVariablesMockWithBmi()
    assert test.run(mock,0) == TestResult(False,
                         "The bmi method get_grid_shape() gives an invalid grid shape.")


def validate_grid_size_condition_test():
    """Test the grid_size_condition test."""
    test = fetch_test("grid_size_condition")
    mock = mocks.BasicModelMockWithBmi()
    assert test.run(mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False,
                               "The method get_grid_size() throws an unexpected error!")
    mock = mocks.BadVariablesMockWithBmi()
    assert test.run(mock,0) == TestResult(False,
                             "The bmi method get_grid_size() does not return a number.")



@pytest.mark.skip()
def validate_grid_type_mismatch_condition_test():
    """Test the grid_type_mismatch_condition test."""
    test = fetch_test("grid_type_mismatch_condition")
    mock = mocks.BasicModelMockWithBmi()
    assert test.run(mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False,
                                       "The method get_grid_type() "
                                       "or get_grid_rank() throws an unexpected error!")
    mock = mocks.BadVariablesMockWithBmi()
    assert test.run(mock,0) == TestResult(False, "The bmi methods get_grid_type() "
                                 "   and get_grid_rank() responses don't fit together!")


def validate_has_required_methods_condition_test():
    """Test the has_required_methods_condition test."""
    test = fetch_test("has_required_methods_condition")
    mock = mocks.BasicModelMockWithBmi()
    assert test.run(mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False,
                      "The model gives an error for checking if all bmi methods exist!")
    mock = mocks.WrongUnitsBmiMock()
    assert test.run(mock,0) == TestResult(False,
                                        "The model does not have all required methods.")


def validate_invalid_grid_rank_condition_test():
    """Test the invalid_grid_rank_condition test."""
    test = fetch_test("invalid_grid_rank_condition")
    mock = mocks.BasicModelMockWithBmi()
    assert test.run(mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False,

                               "The method get_grid_rank() throws an unexpected error!")
    mock = mocks.BadVariablesMockWithBmi()
    assert test.run(mock,0) == TestResult(False,
                                "The bmi method get_grid_rank() gives an invalid rank.")


def validate_invalid_grid_type_condition_test():
    """Test the invalid_grid_type_condition test."""
    test = fetch_test("invalid_grid_type_condition")
    mock = mocks.BasicModelMockWithBmi()
    assert test.run(mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False,
                              "The method get_grid_type() throws an unexpected error!")
    mock = mocks.BadVariablesMockWithBmi()
    assert test.run(mock,0) == TestResult(False,
                                "The bmi method get_grid_type() gives an invalid type.")


def validate_test_get_time_units_test():
    """Test the get_time_units test."""
    test = fetch_test("test_get_time_units")
    mock = mocks.BasicModelMockWithBmi()
    assert test.run(mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False,
                          "The bmi method get_time_units() throws an unexpected error!")
    mock = mocks.WrongUnitsBmiMock()
    assert test.run(mock,0) == TestResult(False,
                            "The bmi method get_time_units() does not return a string.")
    mock = mocks.FaultyTimeMockWithBmi()
    assert test.run(mock,0) == TestResult(False,
                               "The bmi method get_time_units() gives an invalid unit.")
    mock = mocks.FaultyTimeMock2WithBmi()
    assert test.run(mock,0) == TestResult(False,
                     "The bmi method get_time_units() does not include the word since.")


def validate_test_get_value_test():
    """Test the get_value test."""
    test = fetch_test("test_get_value")
    mock = mocks.BasicModelMockWithBmi()
    assert test.run(mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False,
                              "The bmi method get_value() throws an unexpected error!")
    mock = mocks.BadVariablesMockWithBmi()
    assert test.run(mock,0) == TestResult(False,
                            "The bmi method get_value() does not return a numpy array.")


def validate_test_get_value_at_indices_test():
    """Test the get_value_at_indices test."""
    test = fetch_test("test_get_value_at_indices")
    mock = mocks.BasicModelMockWithBmi()
    assert test.run(mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False,
                  "The bmi method get_value_at_indices() throws an unexpected error!")
    mock = mocks.BadVariablesMockWithBmi()
    assert test.run(mock,0) == TestResult(False,
                 "The bmi method get_value_at_indices() does not return a numpy array.")


def validate_test_get_var_grid_test():
    """Test the get_var_grid test."""
    test = fetch_test("test_get_var_grid")
    mock = mocks.BasicModelMockWithBmi()
    assert test.run(mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False,
                            "The bmi method get_var_grid() throws an unexpected error!")
    mock = mocks.BadVariablesMockWithBmi()
    assert test.run(mock,0) == TestResult(False,
                              "The bmi method get_var_grid() does not return a number.")


def validate_test_get_var_itemsize_test():
    """Test the get_var_itemsize test."""
    test = fetch_test("test_get_var_itemsize")
    mock = mocks.BasicModelMockWithBmi()
    assert test.run(mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False,
                        "The bmi method get_var_itemsize() throws an unexpected error!")
    mock = mocks.BadVariablesMockWithBmi()
    assert test.run(mock,0) == TestResult(False,
                          "The bmi method get_var_itemsize() does not return a number.")


def validate_test_get_var_nbytes_test():
    """Test the get_var_nbytes test."""
    test = fetch_test("test_get_var_nbytes")
    mock = mocks.BasicModelMockWithBmi()
    assert test.run(mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False,
                          "The bmi method get_var_nbytes() throws an unexpected error!")
    mock = mocks.BadVariablesMockWithBmi()
    assert test.run(mock,0) == TestResult(False,
                            "The bmi method get_var_nbytes() does not return a number.")


def validate_test_get_var_type_test():
    """Test the get_var_type test."""
    test = fetch_test("test_get_var_type")
    mock = mocks.BasicModelMockWithBmi()
    assert test.run(mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False,
                            "The bmi method get_var_type() throws an unexpected error!")
    mock = mocks.BadVariablesMockWithBmi()
    assert test.run(mock,0) == TestResult(False,
                              "The bmi method get_var_type() does not return a string.")


def validate_test_set_value_test():
    """Test the set_value test."""
    test = fetch_test("test_set_value")
    mock = mocks.BasicModelMockWithBmi()
    assert test.run(mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False,
                               "The bmi method set_value() throws an unexpected error!")


def validate_test_set_value_at_indices_test():
    """Test the set_value_at_indices test."""
    test = fetch_test("test_set_value_at_indices")
    mock = mocks.BasicModelMockWithBmi()
    assert test.run(mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False,
                    "The bmi method set_value_at_indices() throws an unexpected error!")


def validate_time_passage_condition_test():
    """Test the time_passage_condition test."""
    test = fetch_test("time_passage_condition")
    mock = mocks.BasicModelMockWithBmi()
    mock.bmi.finalized = False
    assert test.run(mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False,
                                              "The bmi methods get_current_time() or "
                                              "update() throw an unexpected error!")
    mock = mocks.WrongUnitsBmiMock()
    mock.bmi.finalized = False
    assert test.run(mock,0) == TestResult(False,
                                          "The bmi method get_current_time() does "
                                         "not return a number after an update() call.")
    mock = mocks.FaultyTimeMockWithBmi()
    mock.bmi.finalized = False
    assert test.run(mock,0) == TestResult(False,
                                          "The bmi method get_current_time()"
                                        " gets the wrong time after an update() call.")
