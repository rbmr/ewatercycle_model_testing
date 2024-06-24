import os

import ewatercycle.analysis
import pandas as pd

from plugin_owner_visualise_output_ui import ModelRunnerPopup
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from run_model_util import RunModelUtil
import xarray as xr
import matplotlib.pyplot as plt
import mocks


class VisualiseOutput:

    @staticmethod
    def run(model_name, model_type, parameter_set_name, setup_variables, custom_forcing_name, custom_forcing_variables):
        root = ttk.Window(themename="darkly")
        app = ModelRunnerPopup(root, model_type)
        root.mainloop()
        if app.flag:
            variable_name = app.variable_entry.get()
            start_date = app.start_date_entry.get() + "T00:00:00Z"
            end_date = app.end_date_entry.get() + "T00:00:00Z"
            if model_type == "Distributed":
                graph_type = app.graph_type_var.get()
                if graph_type == "LineGraph":
                    longitude = float(app.longitude_entry.get())
                    latitude = float(app.latitude_entry.get())
            root.destroy()
            print(start_date+" - "+end_date)
            # Temporary Models for testing purposes
            # model = RunModelUtil.getleakymodel(start_date, end_date)
            model = RunModelUtil.get_model_for_visualisation(model_name, model_type, parameter_set_name, setup_variables, custom_forcing_name, custom_forcing_variables, start_date, end_date)
            # model = RunModelUtil.get_wflow_model_time(start_date, end_date)
            if variable_name not in model.output_var_names:
                print("Variable name does not exist: "+variable_name)
                return

            if model_type == "Lumped":
                outputs = RunModelUtil.run_x_array_model(model, variable_name)
                result = xr.concat(outputs, dim="time")
                result.plot()
                plt.savefig(os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                                         (model_name + " LineGraph (" + str(start_date) + " - " + str(end_date) + ")")))
                plt.show()
            else:
                if graph_type == "HeatMap":
                    RunModelUtil.run_basic_model(model)
                    a = model.get_value_as_xarray(variable_name)
                    a.plot()
                    plt.savefig(os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                                             (model_name+" HeatMap ("+str(start_date)+" - "+str(end_date)+")")))
                    plt.show()
                else:
                    output = RunModelUtil.run_x_array_model_coords(model, variable_name, longitude, latitude)
                    plt.plot(output)
                    plt.savefig(os.path.join(os.path.dirname(os.path.abspath(__file__)), "output",
                                             (model_name+" LineGraph ("+str(start_date)+" - "+str(end_date)+")")))
                    plt.show()

        else:
            print("Cancelled")

#
# model_name = 'PCRGlobWB'
# model_type = 'Distributed'
# output_variable_name = 'discharge'
# parameter_set_name = 'pcrglobwb_rhinemeuse_30min'
# setup_variables = {}
# custom_forcing_name = 'PCRGlobWBForcing'
# custom_forcing_variables = {'directory': 'forcing',
#                                         'precipitationNC': 'precipitation_2001to2010.nc',
#                                         'temperatureNC': 'temperature_2001to2010.nc'}
# VisualiseOutput.run(model_name, model_type, parameter_set_name, setup_variables, custom_forcing_name, custom_forcing_variables)