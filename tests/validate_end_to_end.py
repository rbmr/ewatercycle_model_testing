import yaml

from ewatercycle_model_testing import constants as c
from ewatercycle_model_testing.parse_submission import ParseSubmission
from ewatercycle_model_testing.test_suite import TestSuite
import os

THIS_DIR = os.path.dirname(os.path.realpath(__file__))

def validate_end_to_end_wflow():

    test_suite: TestSuite = TestSuite()

    data = yaml.safe_load(open(os.path.join(THIS_DIR, 'exampleWflowSubmissionFile.yml')))
    all_parameters = ParseSubmission.get_parameters_from_submission(data)
    result: dict = test_suite.run_all(**all_parameters)

    assert result[c.SUITE_PASSED_ATTRIBUTE] is True

def validate_end_to_end_leaky_bucket():

    test_suite: TestSuite = TestSuite()

    data = yaml.safe_load(open(os.path.join(THIS_DIR, 'exampleLeakyBucketSubmissionFile.yml')))
    all_parameters = ParseSubmission.get_parameters_from_submission(data)
    result: dict = test_suite.run_all(**all_parameters)

    assert result[c.SUITE_PASSED_ATTRIBUTE] is True
