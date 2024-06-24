"""
A module that has tests that test the test_bank class
"""

import pytest

from ewatercycle_model_testing.test import Test
from ewatercycle_model_testing.test_bank import (
    DuplicateNameTestBankException,
    FinalNameTestBankException,
    NoneNameTestBankException,
    TestBank,
)


@pytest.fixture(autouse=True)
def clean_fixture():
    """
    fixture to reset the test_suite class before each test
    """
    Test.boundInstances.clear()
    Test.existingTestNames.clear()
    TestBank.boundInstances.clear()
    yield

def validate_constructor_name():
    """
    tests if the name gets set correctly with the constructor
    """
    test_bank = TestBank(name="Hello!")
    assert test_bank.name == "Hello!"

def validate_constructor_description():
    """
    tests if the description gets set correctly with the constructor
    """
    test_bank = TestBank(description="Goodbye!")
    assert test_bank.description == "Goodbye!"

def validate_constructor_name_and_description():
    """
    tests if the name and description gets set correctly
    """
    test_bank = TestBank(name="Hello!", description="Goodbye!")
    assert test_bank.name == "Hello!"
    assert test_bank.description == "Goodbye!"

def validate_constructor_empty():
    """
    tests if the name and description are empty when not set
    """
    test_bank = TestBank()
    assert test_bank.name is None
    assert test_bank.description is None

def validate_name():
    """
    tests if the name gets set correctly
    """
    test_bank = TestBank()
    test_bank.name = "Hello!"
    assert test_bank.name == "Hello!"

def validate_none_name():
    """
    test if no name works with constructor and not if set explicitly
    """
    test_bank = TestBank(name=None)  # will work fine.
    with pytest.raises(NoneNameTestBankException):
        test_bank.name = None  # will raise an exception.

def validate_duplicate_name():
    """
    tests if you cant have duplicate names
    """
    test_bank1 = TestBank(name="A")
    with pytest.raises(DuplicateNameTestBankException):
        test_bank2 = TestBank(name="A")

    test_bank1 = TestBank()
    test_bank1.name = "B"
    test_bank2 = TestBank()
    with pytest.raises(DuplicateNameTestBankException):
        test_bank2.name = "B"

def validate_final_name():
    """
    tests if names are final
    """
    test_bank = TestBank(name="A")
    with pytest.raises(FinalNameTestBankException):
        test_bank.name = "B"

    test_bank = TestBank()
    test_bank.name = "C"
    with pytest.raises(FinalNameTestBankException):
        test_bank.name = "D"

def validate_enable_critical():
    """
    tests if the enable_critical flag gets set correctly
    """
    test_bank = TestBank()
    test1 = Test(name="A", critical=False, enabled=False)
    test2 = Test(name="B", critical=False, enabled=True)
    test3 = Test(name="C", critical=True, enabled=False)
    test4 = Test(name="D", critical=True, enabled=True)
    test_bank.tests.append(test1)
    test_bank.tests.append(test2)
    test_bank.tests.append(test3)
    test_bank.tests.append(test4)

    test_bank.enable_critical()
    assert not test1.enabled
    assert test2.enabled
    assert test3.enabled
    assert test4.enabled


def validate_disable_critical():
    """
    tests if the disable_critical flag gets set correctly
    """
    test_bank = TestBank()
    test1 = Test(name="A", critical=False, enabled=False)
    test2 = Test(name="B", critical=False, enabled=True)
    test3 = Test(name="C", critical=True, enabled=False)
    test4 = Test(name="D", critical=True, enabled=True)
    test_bank.tests.append(test1)
    test_bank.tests.append(test2)
    test_bank.tests.append(test3)
    test_bank.tests.append(test4)

    test_bank.disable_critical()
    assert not test1.enabled
    assert test2.enabled
    assert not test3.enabled
    assert not test4.enabled


def validate_enable_all():
    """
    tests if all tests get enabled correctly
    """
    test_bank = TestBank()
    test1 = Test(name="A", critical=False, enabled=False)
    test2 = Test(name="B", critical=False, enabled=True)
    test3 = Test(name="C", critical=True, enabled=False)
    test4 = Test(name="D", critical=True, enabled=True)
    test_bank.tests.append(test1)
    test_bank.tests.append(test2)
    test_bank.tests.append(test3)
    test_bank.tests.append(test4)

    test_bank.enable_all()
    assert test1.enabled
    assert test2.enabled
    assert test3.enabled
    assert test4.enabled

def validate_disable_all():
    """
    tests if all tests get disabled correctly
    """
    test_bank = TestBank()
    test1 = Test(name="A", critical=False, enabled=False)
    test2 = Test(name="B", critical=False, enabled=True)
    test3 = Test(name="C", critical=True, enabled=False)
    test4 = Test(name="D", critical=True, enabled=True)
    test_bank.tests.append(test1)
    test_bank.tests.append(test2)
    test_bank.tests.append(test3)
    test_bank.tests.append(test4)

    test_bank.disable_all()
    assert not test1.enabled
    assert not test2.enabled
    assert not test3.enabled
    assert not test4.enabled

def validate_decorator():
    """
    tests the test decorator of the test class
    """
    test1 = Test(name="A")
    test2 = Test(name="B")
    test3 = Test(name="C")

    class ExampleClass:
        attr1 = test1
        attr2 = test2
        attr3 = test3

    test_bank1 = TestBank()
    test_bank2 = test_bank1(ExampleClass)
    assert test_bank1 is test_bank2
    assert test_bank1.name == ExampleClass.__name__
    assert test_bank1.tests == [test1, test2, test3]
