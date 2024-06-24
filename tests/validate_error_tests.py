"""module containing tests for the SpecTests test bank."""
import pytest

from ewatercycle_model_testing import mocks
from ewatercycle_model_testing.error_tests import ErrorTests
from ewatercycle_model_testing.test_result import TestResult


def fetch_test(test_name):
    """Fetch a test from the spec_tests test bank by its name.

    Args:
       test_name: the name of the test to fetch

    Returns:
        Test: the test with the given name from the spec_tests test bank

    Raises:
        Exception: a test with the given name does not exist in the spec_tests test bank
    """
    for temp in ErrorTests.tests:
        if temp.name == test_name:
            return temp
    raise Exception("that test doesn't exist in the SpecTests bank!")


def validate_incorrect_var_name_condition():
    """Test the incorrect_var_name_condition test."""
    test = fetch_test('incorrect_var_name_condition')
    mock = mocks.BasicModelMock()
    assert test.run(mock, 0).passed is False
    mock = mocks.ErrorThrowerMock()
    assert test.run(mock, 0).passed is True


def validate_incorrect_var_name_condition_bmi():
    """Test the incorrect_var_name_condition_bmi test."""
    test = fetch_test('incorrect_var_name_condition')
    mock = mocks.BasicModelMockWithBmi()
    assert test.run(mock, 0).passed is False
    mock = mocks.ErrorThrowerBmiMock()
    assert test.run(mock, 0).passed is True


def validate_incorrect_var_name_xarray_condition():
    """Test the incorrect_var_name_xarray_condition test."""
    test = fetch_test('incorrect_var_name_xarray_condition')
    mock = mocks.BasicModelMock()
    assert test.run(mock, 0).passed is False
    mock = mocks.ErrorThrowerMock()
    assert test.run(mock, 0).passed is True


def validate_model_runs_to_completion():
    """Test the model_runs_to_completion test."""
    test = fetch_test('model_runs_to_completion')
    mock = mocks.BasicModelMock()
    assert test.run(mock, 0).passed is True
    mock = mocks.ErrorThrowerMock()
    assert test.run(mock, 0).passed is False


def validate_num_outside_array_condition():
    """Test the num_outside_array_condition test."""
    test = fetch_test('num_outside_array_condition')
    mock = mocks.ArrayTooSmallMock()
    assert test.run(mock, 0).passed is False
    mock = mocks.ErrorThrowerMock()
    assert test.run(mock, 0).passed is True


def validate_incorrect_var_name_latlon_condition():
    """Test the num_outside_array_condition test."""
    test = fetch_test('incorrect_var_name_latlon_condition')
    mock = mocks.BasicModelMock()
    assert test.run(mock, 0).passed is False
    mock = mocks.ErrorThrowerMock()
    assert test.run(mock, 0).passed is True


def validate_incorrect_var_name_val_indices_condition_bmi():
    """Test the incorrect_var_name_val_indices_condition_bmi test."""
    test = fetch_test('incorrect_var_name_val_indices_condition_bmi')
    mock = mocks.NoErrorBmiMock()
    assert test.run(mock, 0).passed is False
    mock = mocks.ErrorThrowerBmiMock()
    assert test.run(mock, 0).passed is True


def validate_incorrect_var_name_itemsize_condition_bmi():
    """Test the incorrect_var_name_itemsize_condition_bmi test."""
    test = fetch_test('incorrect_var_name_itemsize_condition_bmi')
    mock = mocks.NoErrorBmiMock()
    assert test.run(mock, 0).passed is False
    mock = mocks.ErrorThrowerBmiMock()
    assert test.run(mock, 0).passed is True


def validate_incorrect_var_name_nbytes_condition_bmi():
    """Test the incorrect_var_name_nbytes_condition_bmi test."""
    test = fetch_test('incorrect_var_name_nbytes_condition_bmi')
    mock = mocks.NoErrorBmiMock()
    assert test.run(mock, 0).passed is False
    mock = mocks.ErrorThrowerBmiMock()
    assert test.run(mock, 0).passed is True
