from sixgill.pipesim import Model, Units
from sixgill.definitions import ModelComponents, Parameters, Constants, SystemVariables, ProfileVariables
import pandas as pd
import os

from ._plot_utility import NA_plot
from ._logger import logger
from ._add_black_oil import add_black_oil
from ._create_ipr import create_ipr
from ._pt_analysis_for_vlp import _pt_analysis_for_vlp
from ._ipr_vlp_matching import ipr_vlp_matching
from ._perform_pt_analysis import perform_pt_analysis
from ._plot_operating_point import plot_operating_point
from ._add_gas_lift import add_gas_lift
from ._install_new_glv import install_new_glv
from ._perform_sensitivity import perform_sensitivity

import warnings
warnings.filterwarnings("ignore")

class WELL_ANALYSIS:
    def __init__(self, well_name, tubing_dia, perforation_depth, packer_depth= None, well_trajectory=None, tubing_shoe_depth=None, casing_dia = 6.18, casing_shoe_depth= None):
        try:
            self.well_name= well_name
            self.perforation_depth= perforation_depth
            if packer_depth is None:
                self.packer_depth= perforation_depth - 100
            else:
                self.packer_depth= packer_depth

            self.model = Model.new(f"{self.well_name}.pips", units= Units.METRIC, overwrite=True)

            if well_trajectory is not None:
                try:
                    self.model.add(ModelComponents.WELL, "main_well")
                    self.model.set_value("main_well", parameter=Parameters.Well.AMBIENTTEMPERATURE, value=30)
                    self.model.set_value("main_well", parameter=Parameters.Well.DeviationSurvey.SURVEYTYPE, value="TwoDimensional")
                    self.model.set_trajectory("main_well", value= well_trajectory)
                except:
                    self.model.set_value("main_well", parameter=Parameters.Well.AMBIENTTEMPERATURE, value=30)
                    self.model.set_value("main_well", parameter=Parameters.Well.DeviationSurvey.SURVEYTYPE, value="TwoDimensional")
                    self.model.set_trajectory("main_well", value= well_trajectory)
            else:
                try:
                    self.model.add(ModelComponents.WELL, "main_well")
                    self.model.set_value("main_well", parameter=Parameters.Well.AMBIENTTEMPERATURE, value=30)
                    self.model.set_value("main_well", parameter=Parameters.Well.DeviationSurvey.SURVEYTYPE, value="VerticalDeviation")
                except:
                    self.model.set_value("main_well", parameter=Parameters.Well.AMBIENTTEMPERATURE, value=30)
                    self.model.set_value("main_well", parameter=Parameters.Well.DeviationSurvey.SURVEYTYPE, value="VerticalDeviation")
                

            if casing_shoe_depth is None:
                self.model.add(ModelComponents.CASING, "Csg1", context="main_well", \
                        parameters={Parameters.Casing.TOPMEASUREDDEPTH:0,
                                    Parameters.Casing.LENGTH:perforation_depth + 5,
                                    Parameters.Casing.INNERDIAMETER:casing_dia*25.4,
                                    Parameters.Casing.BOREHOLEDIAMETER:30*25.4,
                                    Parameters.Casing.WALLTHICKNESS:0.5*25.4})
            else:
                self.model.add(ModelComponents.CASING, "Csg1", context="main_well", \
                        parameters={Parameters.Casing.TOPMEASUREDDEPTH:0,
                                    Parameters.Casing.LENGTH:casing_shoe_depth,
                                    Parameters.Casing.INNERDIAMETER:casing_dia*25.4,
                                    Parameters.Casing.BOREHOLEDIAMETER:30*25.4,
                                    Parameters.Casing.WALLTHICKNESS:0.5*25.4})
            
            if tubing_shoe_depth is None:
                self.model.add(ModelComponents.TUBING, "Tub1", context="main_well", \
                        parameters={Parameters.Tubing.TOPMEASUREDDEPTH:0,
                                    Parameters.Tubing.LENGTH:perforation_depth -5,
                                    Parameters.Tubing.INNERDIAMETER:tubing_dia*25.4,
                                    Parameters.Tubing.WALLTHICKNESS:0.2*25.4})
            else:
                self.model.add(ModelComponents.TUBING, "Tub1", context="main_well", \
                        parameters={Parameters.Tubing.TOPMEASUREDDEPTH:0,
                                    Parameters.Tubing.LENGTH:tubing_shoe_depth,
                                    Parameters.Tubing.INNERDIAMETER:tubing_dia*25.4,
                                    Parameters.Tubing.WALLTHICKNESS:0.2*25.4})
            
            self.model.add(ModelComponents.PACKER, "Packer", context="main_well", parameters={Parameters.Packer.TOPMEASUREDDEPTH:self.packer_depth})

            self.model.save()
            logger.info(f"Initial well model created and saved at {os.getcwd()}")
        except:
            logger.error("Unable to create the base well model/")    

    def add_gas_lift(self, gl_depth, gl_rate):
        return add_gas_lift(self, gl_depth, gl_rate)
    
    def add_black_oil(self, q_gas, q_oil, q_water, api, gg, gas_well= False):
        return add_black_oil(self, q_gas, q_oil, q_water, api, gg, gas_well)

    def create_ipr(self, reservoir_temperature, reservoir_pressure, liquid_pi, fbhp= None):
        return create_ipr(self, reservoir_temperature, reservoir_pressure, liquid_pi, fbhp)

    def _pt_analysis_for_vlp(self, parameters= None, profile_variables= None):
        return _pt_analysis_for_vlp(self, parameters, profile_variables)

    def ipr_vlp_matching(self, thp, fbhp):
        return ipr_vlp_matching(self, thp, fbhp)

    def perform_pt_analysis(self, study_name=None, thp= None, q_gas= None, q_oil= None, q_water= None, api= None, gg= None, gl_depth= None, gl_rate= None):
        return perform_pt_analysis(self, study_name, thp, q_gas, q_oil, q_water, api, gg, gl_depth, gl_rate)

    def plot_operating_point(self, thp=None):
        return plot_operating_point(self, thp)
    
    def install_new_glv(self, gas_injection_pressure, thp=None):
        return install_new_glv(self, gas_injection_pressure, thp)
    
    def perform_sensitivity(self, study_name= None, thp_sensitivity= None, tubing_sensitivity= None, lift_gas_sensitivity= None, watercut_sensitivity= None, GOR_sensitivity= None, reservoir_pressure_sensitivity= None):
        return perform_sensitivity(self, study_name, thp_sensitivity, tubing_sensitivity, lift_gas_sensitivity, watercut_sensitivity, GOR_sensitivity, reservoir_pressure_sensitivity)
    


# if __name__=="__main__":

#     well1= WELL_ANALYSIS("well1", tubing_dia=2.99, perforation_depth=2800, well_trajectory= pd.DataFrame({"MeasuredDepth":[0, 1100, 2200, 3200], "TrueVerticalDepth":[0, 1000, 2000, 2800]}))

#     well1.add_gas_lift(gl_depth=500, gl_rate=5000)

#     well1.add_black_oil(q_gas=90000, q_oil=5, q_water=5, api=30, gg=0.7, gas_well=True)

#     well1.create_ipr(reservoir_pressure=130, fbhp=95, liquid_pi=0.5)

#     well1.ipr_vlp_matching(thp=30, fbhp=52)

#     well1.perform_pt_analysis(study_name="Study 1", thp=30)

#     well1.perform_pt_analysis(study_name="Study 2", thp=35)

#     well1.perform_pt_analysis(study_name="Study 3", thp=25)

#     well1.plot_operating_point()

#     well1.install_new_glv(gas_injection_pressure=50, thp=30)

#     well1.perform_sensitivity(study_name="Study 1", thp_sensitivity=[1, 10], tubing_sensitivity=[2.44, 3.49], lift_gas_sensitivity=[0, 10000], watercut_sensitivity=[0, 50], GOR_sensitivity=[100, 1000], reservoir_pressure_sensitivity=[100, 80])

#     well1.perform_sensitivity(study_name="Study 2", thp_sensitivity=[2, 10], tubing_sensitivity=[2.44, 3.49], lift_gas_sensitivity=[0, 10000], watercut_sensitivity=[0, 50], GOR_sensitivity=[100, 1000], reservoir_pressure_sensitivity=[100, 80])

#     well1.perform_sensitivity(study_name="Study 3", thp_sensitivity=[5, 10], tubing_sensitivity=[2.44, 3.49], lift_gas_sensitivity=[0, 10000], watercut_sensitivity=[0, 50], GOR_sensitivity=[100, 1000], reservoir_pressure_sensitivity=[100, 80])
