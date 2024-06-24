"""
a module that has a ui for enabling and disabling tests
"""

import os.path
import ttkbootstrap as ttk
import yaml
from plugin_owner_select_tests_ui import TestSelector
from run_model_util import RunModelUtil
from test_suite import TestSuite
import constants as c
import ewatercycle
from test_report_maker import GenerateReport




class TestSelect:
    """
    #Run this class to open the UI
    """

    @staticmethod
    def run(model_name, model_type, output_variable_name, parameter_set_name, setup_variables, custom_forcing_name, custom_forcing_variablesin):
        """
        runs the ui
        """
        ts = TestSuite()
        test_dict = TestSelect.get_dictionary(ts)
        app = TestSelect.show_ui(test_dict)

        parameter_set = RunModelUtil.get_parameter_set(parameter_set_name)

        # Don't need shape and start_time/end_time in custom_forcing_variables dictionary!!!

        custom_forcing_variables = RunModelUtil.get_custom_forcing_variables(custom_forcing_variablesin, parameter_set)

        if app.success:
            app.master.destroy()
            TestSelect.enable_disable(ts.tests.values(), app.selected_tests)
            results = ts.run_all(model_name, model_type, output_variable_name,
                                     parameter_set, setup_variables,
                                     custom_forcing_name, custom_forcing_variables)

            if results[c.SUITE_PASSED_ATTRIBUTE]:
                print("tests passed!")
            else:
                print("tests failed!")
            TestSelect.generate_test_report(results, model_name)
        else:
            app.master.destroy()
            print("No tests run due to cancellation or termination")

    @staticmethod
    def get_dictionary(testsuite):
        """
        gets a dictionary of tests
        """
        test_dict = {}
        for tb in testsuite.test_banks.values():
            test_dict[tb.name] = tb.tests

        return test_dict

    @staticmethod
    def show_ui(test_dict):
        """
        shows the ui on screen
        """

        # root = ttk.Window(themename="cyborg")
        root = ttk.Window(themename="darkly")
        app = TestSelector(root, test_dict)
        root.mainloop()
        return app


    @staticmethod
    def enable_disable(tests, selected_tests):
        """
        enables or disables the tests
        """
        for test in tests:
            if test.name in selected_tests:
                test.enabled = True
            else:
                test.enabled = False

    @staticmethod
    def generate_test_report(results, model_name):
        """
        generates the test report
        """
        print("Generating Yaml")
        GenerateReport.generate_report_yaml(yaml.dump(results), os.path.join(os.getcwd(), 'output'))
        print("Generating MarkDown")
        GenerateReport.generate_mark_down(results, os.path.join(os.getcwd(), 'output'), "output", model_name)


# model_name = 'PCRGlobWB'
# model_type = 'Distributed'
# output_variable_name = 'discharge'
# parameter_set_name = 'pcrglobwb_rhinemeuse_30min'
# setup_variables = {}
# custom_forcing_name = 'PCRGlobWBForcing'
# custom_forcing_variables = {'directory': 'forcing',
#                                         'precipitationNC': 'precipitation_2001to2010.nc',
#                                         'temperatureNC': 'temperature_2001to2010.nc'}
# TestSelect.run(model_name, model_type, output_variable_name, parameter_set_name, setup_variables, custom_forcing_name, custom_forcing_variables)
