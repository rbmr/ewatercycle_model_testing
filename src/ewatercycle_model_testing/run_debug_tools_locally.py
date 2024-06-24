from test_suite import TestSuite
from ewatercycle_model_testing.plugin_owner_visualise_output import VisualiseOutput

# These are the test banks, you can add your own by importing it


test_suite: TestSuite = TestSuite()

# Example LeakyBucket Inputs, copy and/or change this to test your model
# For variables that are not used put: None
model_name = 'LeakyBucket'              # Your model class name
model_type = 'Lumped'                   # Type of model: Lumped or Distributed
output_variable_name = 'discharge'      # Output variable name of discharge
parameter_set_name = None               # Name of the used parameter set
setup_variables = {"leakiness": 1}      # Any setup variables used in dictionary form
custom_forcing_name = None              # Name of custom forcing used for the model
custom_forcing_variables = None         # Extra variables needed for the forcing object



# Opens a pop-up that gives an overview of all tests.
# Tests can be enabled and disabled using the checkboxes.
# UNCOMMENT TO RUN
# TestSelect.run(model_name, model_type, output_variable_name, parameter_set_name, setup_variables, custom_forcing_name,   custom_forcing_variables)
# Output is automatically written to the output.md and output.yaml files in the output directory.



# Opens a pop-up that will prompt information about the desired output graph.
# UNCOMMENT TO RUN
VisualiseOutput.run(model_name, model_type, parameter_set_name, setup_variables, custom_forcing_name, custom_forcing_variables)
# Output figures are shown and printed to the output directory.