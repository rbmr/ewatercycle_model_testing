"""
A module that has tests that test the test suite class
"""
import pytest

from ewatercycle_model_testing import constants as c
from ewatercycle_model_testing.test import Test
from ewatercycle_model_testing.test_bank import TestBank
from ewatercycle_model_testing.test_result import TestResult
from ewatercycle_model_testing.test_suite import TestSuite


def example_test() -> TestResult:
    """
    test mock for validating the test_suite class
    """

@pytest.fixture(autouse=True)
def clean_fixture():
    """
    fixture to reset the test_suite class before each test
    """
    Test.boundInstances.clear()
    Test.existingTestNames.clear()
    TestBank.boundInstances.clear()
    if TestSuite._TestSuite__instance:
        TestSuite._TestSuite__instance = None
    yield

def validate_singleton_behavior():
    """
    tests if the singleton behavior of the test_suite is working
    """
    ts1 = TestSuite()
    ts2 = TestSuite()
    assert ts1 is ts2

def validate_initialization():
    """
    tests the initialization of the test_suite
    """
    test_suite = TestSuite()
    assert test_suite.version == c.VERSION
    assert test_suite.tests is Test.boundInstances
    assert test_suite.test_banks is TestBank.boundInstances

def validate_get_test():
    """
    tests get_test() method
    """
    test1 = Test(name="A", run=example_test)
    _ = Test(name="B")
    _ = Test()
    test_suite = TestSuite()
    assert test_suite.get_test("A") is test1
    assert test_suite.get_test("B") is None
    assert test_suite.get_test("C") is None

def validate_get_test_bank():
    """
    tests get_test_bank() method
    """
    test_bank1 = TestBank(name="A")
    _ = TestBank()
    test_suite = TestSuite()
    assert test_suite.get_test_bank("A") is test_bank1
    assert test_suite.get_test_bank("B") is None

def validate_enable_critical():
    """
    tests if the enable_critical() method enables all the critical tests in the test suite
    """
    test1 = Test(name="A", critical=False, enabled=False, run=example_test)
    test2 = Test(name="B", critical=False, enabled=True, run=example_test)
    test3 = Test(name="C", critical=True, enabled=False, run=example_test)
    test4 = Test(name="D", critical=True, enabled=True, run=example_test)
    test_suite = TestSuite()
    test_suite.enable_critical()
    assert not test1.enabled
    assert test2.enabled
    assert test3.enabled
    assert test4.enabled

def validate_disable_critical():
    """
    tests if the disable_critical() method disables only the critical tests in the test suite
    """
    test1 = Test(name="A", critical=False, enabled=False, run=example_test)
    test2 = Test(name="B", critical=False, enabled=True, run=example_test)
    test3 = Test(name="C", critical=True, enabled=False, run=example_test)
    test4 = Test(name="D", critical=True, enabled=True, run=example_test)
    test_suite = TestSuite()
    test_suite.disable_critical()
    assert not test1.enabled
    assert test2.enabled
    assert not test3.enabled
    assert not test4.enabled

def validate_enable_all():
    """
    tests if the enable_all() method enables all tests in the test suite
    """
    test1 = Test(name="A", critical=False, enabled=False, run=example_test)
    test2 = Test(name="B", critical=False, enabled=True, run=example_test)
    test3 = Test(name="C", critical=True, enabled=False, run=example_test)
    test4 = Test(name="D", critical=True, enabled=True, run=example_test)
    test_suite = TestSuite()
    test_suite.enable_all()
    assert test1.enabled
    assert test2.enabled
    assert test3.enabled
    assert test4.enabled

def validate_disable_all():
    """
    tests if the disable_all() method disables all tests in the test suite
    """
    test1 = Test(name="A", critical=False, enabled=False, run=example_test)
    test2 = Test(name="B", critical=False, enabled=True, run=example_test)
    test3 = Test(name="C", critical=True, enabled=False, run=example_test)
    test4 = Test(name="D", critical=True, enabled=True, run=example_test)
    test_suite = TestSuite()
    test_suite.disable_all()
    assert not test1.enabled
    assert not test2.enabled
    assert not test3.enabled
    assert not test4.enabled
