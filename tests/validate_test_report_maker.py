"""
A module that has tests that test the test_report_maker class
"""
import os

import pytest

from ewatercycle_model_testing.test_report_maker import GenerateReport


@pytest.fixture(name="results_test")
def results_test_fixture():
    """
    fixture to have tests for the testing of the test_report_maker class
    """
    return {
        "Test 1":
        {
            "name": "Test 1",
            "description": "This is the first test.",
            "critical": True,
            "enabled": True,
            "passed": False,
            "reason": "Some failure reason."
        },
        "Test 2":
        {
            "name": "Test 2",
            "description": "This is the second test.",
            "critical": False,
            "enabled": True,
            "passed": True,
            "reason": "Passed successfully."
        },
        "Test 3":
        {
            "name": "Test 3",
            "description": "This is the third test.",
            "critical": False,
            "enabled": True,
            "passed": False,
            "reason": "Non critical failed."
        }
    }

def validate_generate_report_yaml():
    """
    tests if a report is generated correctly
    """
    location = GenerateReport.generate_report_yaml(
        "I wrote this", os.getcwd(), "validation")
    file = open(location, 'r')
    file_content = file.read()
    assert file_content == "---\nI wrote this"
    os.remove(location)

def validate_generate_report_yaml_empty_filename():
    """
    tests if report gets generated with empty filename
    """
    location = GenerateReport.generate_report_yaml("I wrote this", os.getcwd())
    file = open(location, 'r')
    file_content = file.read()
    assert file_content == "---\nI wrote this"
    os.remove(location)
def validate_generate_report_yaml_whitespace_filename():
    """
    tests if report gets generated with whitespaces as filename
    """
    location = GenerateReport.generate_report_yaml("I wrote this", os.getcwd(), "     ")
    assert os.path.exists(location)
    file = open(location, 'r')
    file_content = file.read()
    assert file_content == "---\nI wrote this"
    os.remove(location)
def validate_file_exists(results_test):
    """
    tests if the file gets created
    """
    report_file = "randomname.md"
    location = GenerateReport.generate_mark_down(results_test, os.getcwd(),
                                                 report_file, "Random model v1")
    assert os.path.exists(location)
    os.remove(location)
def validate_colors(results_test):
    """
    tests if the colors of the text are correctly applied
    """
    report_file = "randomname.md"
    location = GenerateReport.generate_mark_down(results_test, os.getcwd(),
                                                 report_file, "Random model v1")
    with open(location, 'r') as f:
        content = f.read()

    # Check for the critical test color (red)
    assert "<span style='color:red'>Test 1</span>" in content

    # Check for the non-critical test color (blue)
    assert "<span style='color:green'>Test 2</span>" in content

    assert "<span style='color:orange'>Test 3</span>" in content
    os.remove(location)
