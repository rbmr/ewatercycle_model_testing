"""
A module that has tests that test the test class
"""
import pytest
from ewatercycle.base.model import eWaterCycleModel

from ewatercycle_model_testing import constants as c

#pylint:disable=import-error
from ewatercycle_model_testing.test import (
    DuplicateNameTestException,
    FinalNameTestException,
    FinalRunTestException,
    ForbiddenNameTestException,
    NoneNameTestException,
    NoneRunTestException,
    Test,
    UnboundTestException,
)
from ewatercycle_model_testing.test_result import TestResult


def example_test(model: eWaterCycleModel, discharge_name: str) -> TestResult:
    """
    test example to test the test class that returns a test result class with true
    """
    return TestResult(True)
def example_test1() -> TestResult:
    """
    test example to test the test class that has a passed test result
    """
def example_test2() -> TestResult:
    """
    test example to test the test class that has a passed test result
    """
@pytest.fixture(autouse=True)
def clean_fixture():
    """
    fixture to reset the text instances
    """
    Test.boundInstances.clear()
    Test.existingTestNames.clear()
    yield

def validate_constructor_name():
    """
    tests if the constructor sets the name correctly
    """
    test = Test(name="Something.")
    assert test.name == "Something."

def validate_constructor_description():
    """
    tests if the constructor sets the description correctly
    """
    test = Test(description="Hello!")
    assert test.description == "Hello!"

def validate_constructor_critical():
    """
    tests if the constructor sets the critical exception correctly to true
    """
    test = Test(critical=True)
    assert test.critical

def validate_constructor_non_critical():
    """
    tests if the constructor sets the critical exception correctly to false
    """
    test = Test(critical=False)
    assert not test.critical

def validate_constructor_enabled():
    """
    tests if the constructor sets the enabled exception correctly to true
    """
    test = Test(enabled=True)
    assert test.enabled

def validate_constructor_disabled():
    """
    tests if the constructor sets the disabled exception correctly to false
    """
    test = Test(enabled=False)
    assert not test.enabled

def validate_constructor_run():
    """
    tests if the constructor sets the run exception correctly to a function
    """
    test = Test(run=example_test)
    assert test.run == example_test
    assert test.name == example_test.__name__

def validate_constructor_empty():
    """
    tests an empty constructor
    """
    test = Test()
    assert test.name is None
    assert test.description is None
    assert test.critical is False
    assert test.enabled is True
    assert test.run is None

def validate_none_name():
    """
    tests if the constructor works with no name
    """
    test = Test(name=None) # will work fine.
    with pytest.raises(NoneNameTestException):
        test.name = None # will raise an exception.

def validate_duplicate_name():
    """
    tests if an error is raised if a name is already taken
    """
    test1 = Test(name="A")
    with pytest.raises(DuplicateNameTestException):
        test2 = Test(name="A")

    test1 = Test()
    test1.name = "B"
    test2 = Test()
    with pytest.raises(DuplicateNameTestException):
        test2.name = "B"

def validate_forbidden_name():
    """
    tests if an error is raised if a name is forbidden
    """
    for name in c.FORBIDDEN_TEST_NAMES:

        with pytest.raises(ForbiddenNameTestException):
            Test(name=name)

        test = Test()
        with pytest.raises(ForbiddenNameTestException):
            test.name = name

def validate_final_name():
    """
    tests if an error is raised if a name is final
    """
    test = Test(name="A")
    with pytest.raises(FinalNameTestException):
        test.name = "B"

    test = Test()
    test.name = "C"
    with pytest.raises(FinalNameTestException):
        test.name = "D"

def validate_name():
    """
    tests jf the name gets set correctly
    """
    test = Test()
    test.name = "A"
    assert test.name == "A"

def validate_none_run():
    """
    tests if the constructor works with no run function but cant explicitly set to None
    """
    test = Test(run=None) # will work fine.
    with pytest.raises(NoneRunTestException):
        test.run = None # will raise an exception.

def validate_final_run():
    """
    tests if the run function is final
    """
    test = Test(run=example_test1)
    with pytest.raises(FinalRunTestException):
        test.run = example_test

    test = Test()
    test.run = example_test2
    with pytest.raises(FinalRunTestException):
        test.run = example_test

def validate_run():
    """
    tests if the run function gets run when called
    """
    test = Test()
    test.run = example_test
    assert test.run == example_test
    assert test.name == example_test.__name__

    test = Test(name="A")
    test.run = example_test
    assert test.run == example_test
    assert test.name == "A"

def validate_call():
    """
    tests if the run function gets run when called
    """
    test1 = Test()
    test2 = test1(example_test)
    assert test1 is test2
    assert test2.run == example_test
    assert test2.name == example_test.__name__

def validate_decorator():
    """
    tests if the decorator works correctly
    """
    # will pass if and only if test_call passes
    test = Test()

    @test
    def example_test3() -> TestResult:
        pass

    assert example_test3 is test
    assert test.name == "example_test3"

def validate_unbound_start():
    """
    tests if an exception is raised when a test does not have a run function
    """
    test = Test()
    with pytest.raises(UnboundTestException):
        test.start(None, None)

def validate_start():
    """
    tests if the constructor works correctly for all variables and runs correctly
    """
    test = Test(name="A", description="B",
                critical=True, enabled=False, run=example_test)
    result = test.start(None, None)
    assert test.test_result is not None
    assert result["name"] == test.name
    assert result["description"] == test.description
    assert result["critical"] == test.critical
    assert result["enabled"] == test.enabled
    assert result["passed"] == test.test_result.passed
    assert result["reason"] == test.test_result.reason
