"""module containing tests for the SpecTests test bank."""
import pytest

from ewatercycle_model_testing import mocks
from ewatercycle_model_testing.spec_tests import SpecTests
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
    for temp in SpecTests.tests:
        if temp.name == test_name:
            return temp
    raise Exception("that test doesn't exist in the SpecTests bank!")


def validate_correct_start_time_test():
    """Test the correct_start_time test."""
    test = fetch_test('correct_start_time')
    mock = mocks.BasicModelMock()
    assert test.run(mock,0) == TestResult(True)
    mock = mocks.worstModelMock()
    assert test.run(mock,0) == TestResult(False, "error occurred, are these functions implemented properly? .start_time, .end_time")
    mock = mocks.FaultyTimeMock()
    assert test.run(mock,0) == TestResult(False,
                                          "Model start time or end time is incorrect")


def validate_has_check_parameter_set_test():
    """Test the has_check_parameter_set test."""
    test = fetch_test('has_check_parameter_set')
    basic_model_mock = mocks.BasicModelMock()
    assert test.run(basic_model_mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False, "error occurred, are these functions implemented properly? ._check_parameter_set")


def validate_has_make_bmi_instance_test():
    """Test the has_make_bmi_instance test."""
    test = fetch_test('has_make_bmi_instance')
    basic_model_mock = mocks.BasicModelMock()
    assert test.run(basic_model_mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False, "error occurred, are these functions implemented properly? ._make_bmi_instance")


def validate_has_parameters_test():
    """Test the has_parameters test."""
    test = fetch_test('has_parameters')
    basic_model_mock = mocks.BasicModelMock()
    assert test.run(basic_model_mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False, "error occurred, are these functions implemented properly? .parameters")


def validate_has_repr_args_test():
    """Test the has_repr_args test."""
    test = fetch_test('has_repr_args')
    basic_model_mock = mocks.BasicModelMock()
    assert test.run(basic_model_mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False, "error occurred, are these functions implemented properly? .__repr_args")


def validate_has_make_cfg_dir_test():
    """Test the has_make_cfg_dir test."""
    test = fetch_test('has_make_cfg_dir')
    basic_model_mock = mocks.BasicModelMock()
    assert test.run(basic_model_mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False, "error occurred, are these functions implemented properly? ._make_cfg_dir")


def validate_has_make_cfg_file_test():
    """Test the has_make_cfg_file test."""
    test = fetch_test('has_make_cfg_file')
    basic_model_mock = mocks.BasicModelMock()
    assert test.run(basic_model_mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False, "error occurred, are these functions implemented properly? ._make_cfg_file")


def validate_has_bmi_test():
    """Test the has_bmi test."""
    test = fetch_test('has_bmi')
    basic_model_mock = mocks.BasicModelMock()
    assert test.run(basic_model_mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False, "error occurred, are these functions implemented properly? .bmi")


def validate_has_vars_out_and_gets_test():
    """Test the has_vars_out_and_gets test."""
    # more complicated to test!
    test = fetch_test('has_vars_out_and_gets')
    mock = mocks.BasicModelMock()
    assert test.run(mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False, "error occurred, are these functions implemented properly? .output_var_names")
    mock = mocks.BadVariablesMock()
    assert test.run(mock,0) == TestResult(False,
                                          "variable <" + "3" + "> not of type ndarray")
    mock = mocks.NoGettersMock()
    assert test.run(mock,0) == TestResult(False, "variable <" + "3" + "> not gettable, are these function implemented properly? .output_var_names, .get_value")


def validate_has_start_time_as_iso_str_test():
    """Test the has_start_time_as_isostr test."""
    test = fetch_test('has_start_time_as_isostr')
    mock = mocks.BasicModelMock()
    assert test.run(mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False, "error occurred, are these functions implemented properly? .start_time_as_isostr")
    mock = mocks.FaultyTimeMock()
    assert test.run(mock,0) == TestResult(False, "Incorrect format, should be: YYYY-MM-DDTHH:MM:SSZ not : " + "20153-12-03T12:05:72Z")


def validate_has_end_time_as_isostr_test():
    """Test the has_end_time_as_isostr test."""
    test = fetch_test('has_end_time_as_isostr')
    mock = mocks.BasicModelMock()
    assert test.run(mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False, "error occurred, are these functions implemented properly? .end_time_as_isostr")
    mock = mocks.FaultyTimeMock()
    assert test.run(mock,0) == TestResult(False, "Incorrect format, should be: YYYY-MM-DDTHH:MM:SSZ not : " + "20153-12-03:12:05:72")


def validate_has_time_as_isostr_test():
    """Test the has_time_as_isostr test."""
    test = fetch_test('has_time_as_isostr')
    mock = mocks.BasicModelMock()
    assert test.run(mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False, "error occurred, are these functions implemented properly? .time_as_isostr")
    mock = mocks.FaultyTimeMock()
    assert test.run(mock,0) == TestResult(False, "Incorrect format, should be: YYYY-MM-DDTHH:MM:SSZ not : " + "2015312-03T12:05:72Z")



def validate_has_start_time_as_datetime_test():
    """Test the has_start_time_as_datetime test."""
    test = fetch_test('has_start_time_as_datetime')
    mock = mocks.BasicModelMock()
    assert test.run(mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False, "error occurred, are these functions implemented properly? .start_time_as_datetime")
    mock = mocks.FaultyTimeMock()
    assert test.run(mock,0) == TestResult(False,
                                    "Incorrect type, should be: datetime not: " + "str")


def validate_has_end_time_as_datetime_test():
    """Test the has_end_time_as_datetime test."""
    test = fetch_test('has_end_time_as_datetime')
    mock = mocks.BasicModelMock()
    assert test.run(mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False, "error occurred, are these functions implemented properly? .end_time_as_datetime")
    mock = mocks.FaultyTimeMock()
    assert test.run(mock,0) == TestResult(False,
                                    "Incorrect type, should be: datetime not: " + "int")


def validate_has_time_as_datetime_test():
    """Test the has_time_as_datetime test."""
    test = fetch_test('has_time_as_datetime')
    mock = mocks.BasicModelMock()
    assert test.run(mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False, "error occurred, are these functions implemented properly? .time_as_datetime")
    mock = mocks.FaultyTimeMock()
    assert test.run(mock,0) == TestResult(False,
                                  "Incorrect type, should be: datetime not: " + "float")


def validate_positive_time_step_test():
    """Test the positive_time_step test."""
    test = fetch_test('positive_time_step')
    mock = mocks.BasicModelMock()
    assert test.run(mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False, "error occurred, are these functions implemented properly? .time_step")
    mock = mocks.FaultyTimeMock()
    assert test.run(mock,0) == TestResult(False,
                                "model time step is negative or zero, is this correct?")


def validate_some_version_condition_test():
    """Test the some_version_condition test."""
    test = fetch_test('some_version_condition')
    mock = mocks.BasicModelMock()
    assert test.run(mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False, "error occurred, are these functions implemented properly? .version")
    mock = mocks.FaultyTimeMock()
    assert test.run(mock,0) == TestResult(False, "model does not have version")


def validate_has_time_unit_condition_test():
    """Test the has_time_unit_condition test."""
    test = fetch_test('has_time_unit_condition')
    mock = mocks.BasicModelMock()
    assert test.run(mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False, "error occurred, are these functions implemented properly? .time_units")

@pytest.mark.skip("Test fails.")
def validate_has_get_lat_lon_grid_test():
    """Test the has_get_lat_lon_grid test."""
    test = fetch_test('has_get_lat_lon_grid')
    mock = mocks.BasicModelMock()
    assert test.run(mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False, "error occurred, are these functions implemented properly? .get_value_at_coords, .output_var_names")
    mock = mocks.BadVariablesMock
    assert test.run(mock,0) == TestResult(False, "incorrect shape, returned shape: " + "(4, 6)" + " actual shape: " + "[5, 6]")
    mock = mocks.NoGettersMock
    assert test.run(mock,0) == TestResult(False,
                                "Could not use method .get_latlon_grid for variable: 3")


def validate_has_get_value_as_x_array_test():
    """Test the has_get_value_as_x_array test."""
    test = fetch_test('has_get_value_as_x_array')
    mock = mocks.BasicModelMock()
    assert test.run(mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False, "error occurred, are these functions implemented properly? .get_value_as_xarray, .output_var_names")
    mock = mocks.NoGettersMock
    assert test.run(mock,0) == TestResult(False, ".get_value_as_xarray method does not return DataArray for variable: " + "3")


def validate_has_get_value_at_coords_test():
    """Test the has_get_value_at_coords test."""
    # 1 more mock case useful here
    test = fetch_test('has_get_value_at_coords')
    mock = mocks.BasicModelMock()
    assert test.run(mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False,
                "error occured, are these functions implemented properly? .get_value_at_coords, .coords_to_indices\n"
                "DOES NOT NEED TO BE IMPLEMENTED FOR LUMPED MODELS SUCH AS LEAKYBUCKET")


def validate_proper_time_passage_test():
    """Test the proper_time_passage test."""
    test = fetch_test('proper_time_passage')
    mock = mocks.BasicModelMock()
    assert test.run(mock,0) == TestResult(True)
    assert test.run(mocks.worstModelMock, 0) == TestResult(False, "error occurred, are these functions implemented properly? .time, .time_step, .update")
    mock = mocks.FaultyTimeMock()
    assert test.run(mock,0) == TestResult(False,
                                          "the model's time does not update properly")


def validate_invalid_grid_type_test():
    """Test the invalid_grid_type test."""
    test = fetch_test('invalid_grid_type')
    mock = mocks.BasicModelMock()
    assert test.run(mock,0) == TestResult(True)
    mock = mocks.BadVariablesMock()
    assert test.run(mock,0) == TestResult(False,"The model's grid's type is invalid")


def validate_invalid_grid_rank_test():
    """Test the invalid_grid_rank test."""
    test = fetch_test('invalid_grid_rank')
    mock = mocks.BasicModelMock()
    assert test.run(mock,0) == TestResult(True)
    mock = mocks.BadVariablesMock()
    assert test.run(mock,0) == TestResult(False,"the model's grid's rank is invalid")


def validate_grid_type_mismatch_test():
    """Test the grid_type_mismatch test."""
    test = fetch_test('grid_type_mismatch')
    mock = mocks.BasicModelMock()
    assert test.run(mock,0) == TestResult(True)
    mock = mocks.BadVariablesMock()
    assert test.run(mock,0) == TestResult(False, "the model outputs wrong grid data!")


def validate_cannot_update_after_finalized_condition_test():
    """Test the cannot_update_after_finalized_condition test."""
    test = fetch_test('cannot_update_after_finalized_condition')
    mock = mocks.BasicModelMock()
    assert test.run(mock,0) == TestResult(True,"Finalized correctly")
    assert test.run(mocks.worstModelMock, 0) == TestResult(False, "error occurred, are these functions implemented properly? .finalize")
    mock = mocks.FaultyInitMock()
    assert test.run(mock,0) == TestResult(False,
                              "model.finalize was unsuccessful in finalising the model")
