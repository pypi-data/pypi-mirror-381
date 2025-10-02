A=None
from sixgill.pipesim import Model,Units
from sixgill.definitions import ModelComponents,Parameters,Constants,SystemVariables,ProfileVariables
import pandas as B,os
from._plot_utility import NA_plot
from._logger import logger
from._add_black_oil import add_black_oil
from._create_ipr import create_ipr
from._pt_analysis_for_vlp import _pt_analysis_for_vlp
from._ipr_vlp_matching import ipr_vlp_matching
from._perform_pt_analysis import perform_pt_analysis
from._plot_operating_point import plot_operating_point
from._add_gas_lift import add_gas_lift
from._install_new_glv import install_new_glv
from._perform_sensitivity import perform_sensitivity
import warnings
warnings.filterwarnings('ignore')
class WELL_ANALYSIS:
	def __init__(B,well_name,tubing_dia,perforation_depth,packer_depth=A,well_trajectory=A,tubing_shoe_depth=A,casing_dia=6.18,casing_shoe_depth=A):
		N='Tub1';M='Csg1';L='VerticalDeviation';K='TwoDimensional';J=casing_shoe_depth;I=casing_dia;H=tubing_shoe_depth;G=packer_depth;F=tubing_dia;E=well_trajectory;D=perforation_depth;C='main_well'
		try:
			B.well_name=well_name;B.perforation_depth=D
			if G is A:B.packer_depth=D-100
			else:B.packer_depth=G
			B.model=Model.new(f"{B.well_name}.pips",units=Units.METRIC,overwrite=True)
			if E is not A:
				try:B.model.add(ModelComponents.WELL,C);B.model.set_value(C,parameter=Parameters.Well.AMBIENTTEMPERATURE,value=30);B.model.set_value(C,parameter=Parameters.Well.DeviationSurvey.SURVEYTYPE,value=K);B.model.set_trajectory(C,value=E)
				except:B.model.set_value(C,parameter=Parameters.Well.AMBIENTTEMPERATURE,value=30);B.model.set_value(C,parameter=Parameters.Well.DeviationSurvey.SURVEYTYPE,value=K);B.model.set_trajectory(C,value=E)
			else:
				try:B.model.add(ModelComponents.WELL,C);B.model.set_value(C,parameter=Parameters.Well.AMBIENTTEMPERATURE,value=30);B.model.set_value(C,parameter=Parameters.Well.DeviationSurvey.SURVEYTYPE,value=L)
				except:B.model.set_value(C,parameter=Parameters.Well.AMBIENTTEMPERATURE,value=30);B.model.set_value(C,parameter=Parameters.Well.DeviationSurvey.SURVEYTYPE,value=L)
			if J is A:B.model.add(ModelComponents.CASING,M,context=C,parameters={Parameters.Casing.TOPMEASUREDDEPTH:0,Parameters.Casing.LENGTH:D+5,Parameters.Casing.INNERDIAMETER:I*25.4,Parameters.Casing.BOREHOLEDIAMETER:762.,Parameters.Casing.WALLTHICKNESS:12.7})
			else:B.model.add(ModelComponents.CASING,M,context=C,parameters={Parameters.Casing.TOPMEASUREDDEPTH:0,Parameters.Casing.LENGTH:J,Parameters.Casing.INNERDIAMETER:I*25.4,Parameters.Casing.BOREHOLEDIAMETER:762.,Parameters.Casing.WALLTHICKNESS:12.7})
			if H is A:B.model.add(ModelComponents.TUBING,N,context=C,parameters={Parameters.Tubing.TOPMEASUREDDEPTH:0,Parameters.Tubing.LENGTH:D-5,Parameters.Tubing.INNERDIAMETER:F*25.4,Parameters.Tubing.WALLTHICKNESS:5.08})
			else:B.model.add(ModelComponents.TUBING,N,context=C,parameters={Parameters.Tubing.TOPMEASUREDDEPTH:0,Parameters.Tubing.LENGTH:H,Parameters.Tubing.INNERDIAMETER:F*25.4,Parameters.Tubing.WALLTHICKNESS:5.08})
			B.model.add(ModelComponents.PACKER,'Packer',context=C,parameters={Parameters.Packer.TOPMEASUREDDEPTH:B.packer_depth});B.model.save();logger.info(f"Initial well model created and saved at {os.getcwd()}")
		except:logger.error('Unable to create the base well model/')
	def add_gas_lift(A,gl_depth,gl_rate):return add_gas_lift(A,gl_depth,gl_rate)
	def add_black_oil(A,q_gas,q_oil,q_water,api,gg,gas_well=False):return add_black_oil(A,q_gas,q_oil,q_water,api,gg,gas_well)
	def create_ipr(A,reservoir_temperature,reservoir_pressure,liquid_pi,fbhp=A):return create_ipr(A,reservoir_temperature,reservoir_pressure,liquid_pi,fbhp)
	def _pt_analysis_for_vlp(A,parameters=A,profile_variables=A):return _pt_analysis_for_vlp(A,parameters,profile_variables)
	def ipr_vlp_matching(A,thp,fbhp):return ipr_vlp_matching(A,thp,fbhp)
	def perform_pt_analysis(A,study_name=A,thp=A,q_gas=A,q_oil=A,q_water=A,api=A,gg=A,gl_depth=A,gl_rate=A):return perform_pt_analysis(A,study_name,thp,q_gas,q_oil,q_water,api,gg,gl_depth,gl_rate)
	def plot_operating_point(A,thp=A):return plot_operating_point(A,thp)
	def install_new_glv(A,gas_injection_pressure,thp=A):return install_new_glv(A,gas_injection_pressure,thp)
	def perform_sensitivity(A,study_name=A,thp_sensitivity=A,tubing_sensitivity=A,lift_gas_sensitivity=A,watercut_sensitivity=A,GOR_sensitivity=A,reservoir_pressure_sensitivity=A):return perform_sensitivity(A,study_name,thp_sensitivity,tubing_sensitivity,lift_gas_sensitivity,watercut_sensitivity,GOR_sensitivity,reservoir_pressure_sensitivity)