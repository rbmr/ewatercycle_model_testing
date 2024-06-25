"""
A module with the main function where the system gets run from.
"""

import os.path
import yaml
import ewatercycle

from ewatercycle_model_testing import parse_submission
from ewatercycle_model_testing.run_model_util import RunModelUtil
from ewatercycle_model_testing.test_suite import TestSuite
from ewatercycle_model_testing.test_report_maker import GenerateReport
from ewatercycle_model_testing.parse_submission import ParseSubmission
from ewatercycle_model_testing import constants as c
#pylint:disable=unused-import
from ewatercycle_model_testing import spec_tests, metric_tests, bmi_spec_tests, scenario_tests, error_tests


def main():
    """
    the main function of the program.
    """
    test_suite: TestSuite = TestSuite()

    # Necessary inputs from github request are the following:
    # model_name, model_type ,output_variable_name, parameter_set_name,
    # setup_variables, custom_forcing_name, custom_forcing_variables
    # If they are not relevant set them to None

    # Example LeakyBucket Input's
    # model_name = 'LeakyBucket'
    # model_type = 'Lumped'
    # output_variable_name = 'discharge'
    # parameter_set_name = ''
    # setup_variables = {"leakiness": 1}
    # custom_forcing_name = None

    # Example Wflow Inputs's
    # model_name = 'Wflow'
    # model_type = 'Distributed'
    # output_variable_name = 'RiverRunoff'
    # parameter_set_name = 'wflow_rhine_sbm_nc'
    # setup_variables = {}
    # custom_forcing_name = 'WflowForcing'
    # custom_forcing_variables = {'directory': parameter_set.directory / '.',
    #                             'netcdfinput': "inmaps.nc",
    #                             'Precipitation': "/P",
    #                             'EvapoTranspiration': "/PET",
    #                             'Temperature': "/TEMP"}

    # # Example PCRGLOB Inputs's
    # model_name = 'PCRGlobWB'
    # model_type = 'Distributed'
    # output_variable_name = 'discharge'
    # parameter_set_name = 'pcrglobwb_rhinemeuse_30min'
    # setup_variables = {}
    # custom_forcing_name = 'PCRGlobWBForcing'
    # custom_forcing_variables = {'directory': (parameter_set.directory / 'forcing'),
    #                             'precipitationNC': 'precipitation_2001to2010.nc',
    #                             'temperatureNC': 'temperature_2001to2010.nc'}

    # Don't need shape and start_time/end_time in custom_forcing_variables dictionary!!!

    # result: dict = test_suite.run_all(model_name, model_type, output_variable_name, parameter_set, setup_variables, custom_forcing_name, custom_forcing_variables)

    # To run LeakyBucket To Debug, Uncomment The Line Below And Comment The Normal RunAll
    # result: dict = test_suite.run_all(**(RunModelUtil.get_leaky_bucket_run_all()))
    # To run Wflow To Debug, Uncomment The Line Below And Comment The Normal RunAll
    # result: dict = test_suite.run_all(**(RunModelUtil.get_wflow_run_all()))

    data = yaml.safe_load(open('workflows/submission.yml'))
    all_parameters = ParseSubmission.get_parameters_from_submission(data)
    result: dict = test_suite.run_all(**all_parameters)

    if result[c.SUITE_PASSED_ATTRIBUTE]:
        # some sort of verification that lets the system know that
        # the branch is tested and can be removed from db
        print("tests passed!")
    else:
        print("tests failed!")

    # you can add a filename as extra argument, otherwise filename will be testReport
    print("Generating Yaml")
    GenerateReport.generate_report_yaml(yaml.dump(result), os.path.join(os.getcwd(), 'output'))
    print("Generating MarkDown")
    GenerateReport.generate_mark_down(result, os.path.join(os.getcwd(), 'output'),
                                      "src/ewatercycle_model_testing/output", data["model_name"])

if __name__ == "__main__":
    main()