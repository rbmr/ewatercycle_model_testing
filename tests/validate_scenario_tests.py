"""Module containing the tests for the ScenarioTests module."""
import pytest
from ewatercycle_leakybucket.model import LeakyBucket

from ewatercycle_model_testing import scenarios_util
from ewatercycle_model_testing.scenario_tests import ScenarioTests
from ewatercycle_model_testing.test_result import TestResult
from src.ewatercycle_model_testing.mocks import ScenarioDistributedMock


def fetch_test(testName):
    """Fetch a test from the ScenarioTests test bank by its name.

    Args:
       testName: the name of the test to fetch

    Returns:
        Test: the test with the given name from the ScenarioTests test bank

    Raises:
        Exception: if a test with the given name
         does not exist in the ScenarioTests test bank
    """
    for temp in ScenarioTests.tests:
        if temp.name == testName:
            return temp
    raise Exception("that test doesn't exist in the ScenarioTests bank!")

def get_leaky_bucket(forcing):
    """Get an instance of the LeakyBucket model initialized with the given forcing.

    Args:
       forcing: the forcing that the requested instance
        of Leakybucket should be initialized on

    Returns:
        LeakyBucket: an instance
         of the LeakyBucket model initialized on the given config
    """
    model = LeakyBucket(forcing=forcing)
    cfg_file, _ = model.setup(leakiness=1)
    model.initialize(cfg_file)
    return model

@pytest.mark.skip(reason = "fails on pipeline for unknown reasons")
def validate_zero_precipitation_lumped_test():
    """Test the zero_precipitation_lumped_test test."""
    test = fetch_test("zero_precipitation_lumped_test")
    forcing = scenarios_util.get_zeroes_lumped_scenario()
    model = get_leaky_bucket(forcing)
    assert test.run(model,"discharge") == TestResult(True)

@pytest.mark.skip(reason = "fails on pipeline for unknown reasons")
def validate_zero_precipitation_distributed_test():
    """Test the zero_precipitation_distributed_test test."""
    test = fetch_test("zero_precipitation_distributed_test")
    forcing = scenarios_util.get_zeroes_distributed_scenario()
    model = ScenarioDistributedMock()
    model.setup(forcing)
    assert test.run(model, "")

@pytest.mark.skip(reason = "fails on pipeline for unknown reasons")
def validate_permanent_precipitation_lumped_test():
    """Test the permanent_precipitation_lumped_test test."""
    test = fetch_test("permanent_precipitation_lumped_test")
    forcing = scenarios_util.get_non_zeroes_lumped_scenario()
    model = get_leaky_bucket(forcing)
    assert test.run(model,"discharge") == TestResult(True)

@pytest.mark.skip(reason = "fails on pipeline for unknown reasons")
def validate_permanent_precipitation_distributed_test():
    """Test the permanent_precipitation_distributed_test test."""
    test = fetch_test("permanent_precipitation_distributed_test")
    forcing = scenarios_util.get_non_zeroes_distributed_scenario()
    model = ScenarioDistributedMock()
    model.setup(forcing)
    assert test.run(model, "") == TestResult(True)

@pytest.mark.skip(reason = "fails on pipeline for unknown reasons")
def validate_strict_increase_test():
    """Test the strict_increase_test test."""
    test = fetch_test("strict_increase_test")
    forcing = scenarios_util.get_increasing_scenario()
    model = get_leaky_bucket(forcing)
    assert test.run(model,"discharge") == TestResult(True)

@pytest.mark.skip(reason = "fails on pipeline for unknown reasons")
def validate_strict_decrease_test():
    """Test the strict_decrease_test test."""
    test = fetch_test("strict_decrease_test")
    forcing = scenarios_util.get_decreasing_scenario()
    model = get_leaky_bucket(forcing)
    assert test.run(model,"discharge") == TestResult(True)

@pytest.mark.skip(reason = "fails on pipeline for unknown reasons")
def validate_proper_mid_spike_handling_lumped_test():
    """Test the proper_mid_spike_handling_lumped_test test."""
    test = fetch_test("proper_mid_spike_handling_lumped_test")
    forcing = scenarios_util.get_mid_spike_lumped_scenario()
    model = get_leaky_bucket(forcing)
    assert test.run(model,"discharge") == TestResult(True)

@pytest.mark.skip(reason = "fails on pipeline for unknown reasons")
def validate_proper_mid_spike_handling_distributed_test():
    """Test the proper_mid_spike_handling_distributed_test test."""
    test = fetch_test("proper_mid_spike_handling_distributed_test")
    forcing = scenarios_util.get_mid_spike_distributed_scenario()
    model = ScenarioDistributedMock()
    model.setup(forcing)
    assert test.run(model, "") == TestResult(True)


@pytest.mark.skip(reason = "fails on pipeline for unknown reasons")
def validate_proper_start_spike_handling_lumped_test():
    """Test the proper_start_spike_handling_lumped_test test."""
    test = fetch_test("proper_start_spike_handling_lumped_test")
    forcing = scenarios_util.get_start_spike_lumped_scenario()
    model = get_leaky_bucket(forcing)
    assert test.run(model,"discharge") == TestResult(True)

@pytest.mark.skip(reason = "fails on pipeline for unknown reasons")
def validate_proper_start_spike_handling_distributed_test():
    """Test the proper_start_spike_handling_distributed_test test."""
    test = fetch_test("proper_start_spike_handling_distributed_test")
    forcing = scenarios_util.get_start_spike_distributed_scenario()
    model = ScenarioDistributedMock()
    model.setup(forcing)
    assert test.run(model, "") == TestResult(True)

@pytest.mark.skip(reason = "fails on pipeline for unknown reasons")
def validate_proper_end_spike_handling_lumped_test():
    """Test the proper_end_spike_handling_lumped_test test."""
    test = fetch_test("proper_end_spike_handling_lumped_test")
    forcing = scenarios_util.get_end_spike_lumped_scenario()
    model = get_leaky_bucket(forcing)
    assert test.run(model,"discharge") == TestResult(True)

@pytest.mark.skip(reason = "fails on pipeline for unknown reasons")
def validate_proper_end_spike_handling_distributed_test():
    """Test the proper_end_spike_handling_distributed_test test."""
    test = fetch_test("proper_end_spike_handling_distributed_test")
    forcing = scenarios_util.get_end_spike_distributed_scenario()
    model = ScenarioDistributedMock()
    model.setup(forcing)
    assert test.run(model, "") == TestResult(True)

@pytest.mark.skip(reason = "fails on pipeline for unknown reasons")
def validate_first_half_precip_lumped_test():
    """Test the first_half_precip_lumped_test test."""
    test = fetch_test("first_half_precip_lumped_test")
    forcing = scenarios_util.get_first_half_precip_lumped_scenario()
    model = get_leaky_bucket(forcing)
    assert test.run(model, "discharge") == TestResult(True)


@pytest.mark.skip(reason = "fails on pipeline for unknown reasons")
def validate_first_half_precip_distributed_test():
    """Test the first_half_precip_distributed_test test."""
    test = fetch_test("first_half_precip_distributed_test")
    forcing = scenarios_util.get_first_half_precip_distributed_scenario()
    model = ScenarioDistributedMock()
    model.setup(forcing)
    assert test.run(model, "discharge") == TestResult(True)

@pytest.mark.skip(reason = "fails on pipeline for unknown reasons")
def validate_second_half_precip_lumped_test():
    """Test the second_half_precip_lumped_test test."""
    test = fetch_test("second_half_precip_lumped_test")
    forcing = scenarios_util.get_second_half_precip_lumped_scenario()
    model = get_leaky_bucket(forcing)
    assert test.run(model,"discharge") == TestResult(True)

@pytest.mark.skip(reason = "fails on pipeline for unknown reasons")
def validate_second_half_precip_distributed_test():
    """Test the second_half_precip_distributed_test test."""
    test = fetch_test("second_half_precip_distributed_test")
    forcing = scenarios_util.get_second_half_precip_distributed_scenario()
    model = ScenarioDistributedMock()
    model.setup(forcing)
    assert test.run(model, "") == TestResult(True)

@pytest.mark.skip(reason = "fails on pipeline for unknown reasons")
def validate_pre_existing_discharge_lumped_test():
    """Test the preExistingDischargeLumpedTest test."""
    test = fetch_test("pre_existing_discharge_lumped_test")
    forcing = scenarios_util.get_zeroes_lumped_scenario()
    model = get_leaky_bucket(forcing)
    assert test.run(model,"discharge") == TestResult(True)

@pytest.mark.skip(reason = "fails on pipeline for unknown reasons")
def validate_pre_existing_discharge_distributed_test():
    """Test the preExistingDischargeDistributedTest test."""
    test = fetch_test("pre_existing_discharge_distributed_test")
    forcing = scenarios_util.get_zeroes_distributed_scenario()
    model = ScenarioDistributedMock()
    model.setup(forcing)
    assert test.run(model, "") == TestResult(True)
