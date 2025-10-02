F=None
from._logger import logger
from sixgill.definitions import ModelComponents,Parameters,Constants
def create_ipr(self,reservoir_temperature,reservoir_pressure,liquid_pi,fbhp=F):
	E=1.;D=fbhp;C=liquid_pi;B='VertComp1';A=self
	try:
		A.reservoir_pressure=reservoir_pressure*.980665+1.01325;A.reservoir_temperature=reservoir_temperature
		if D is not F and C is F:D=D*.980665+1.01325;C=(A.q_oil+A.q_water)/(A.reservoir_pressure-D)
		try:
			if A.gas_well==True:A.model.sim_settings.global_flow_correlation({Parameters.FlowCorrelation.Multiphase.Vertical.CORRELATION:Constants.MultiphaseFlowCorrelation.BakerJardine.GRAY_MODIFIED,Parameters.FlowCorrelation.Multiphase.Vertical.FRICTIONFACTOR:E,Parameters.FlowCorrelation.Multiphase.Vertical.HOLDUPFACTOR:E})
			else:A.model.sim_settings.global_flow_correlation({Parameters.FlowCorrelation.Multiphase.Vertical.CORRELATION:Constants.MultiphaseFlowCorrelation.BakerJardine.DUNSROS,Parameters.FlowCorrelation.Multiphase.Vertical.FRICTIONFACTOR:E,Parameters.FlowCorrelation.Multiphase.Vertical.HOLDUPFACTOR:E})
			A.model.add(ModelComponents.COMPLETION,B,context='main_well',parameters={Parameters.Completion.TOPMEASUREDDEPTH:A.perforation_depth,Parameters.Completion.FLUIDENTRYTYPE:Constants.CompletionFluidEntry.SINGLEPOINT,Parameters.Completion.GEOMETRYPROFILETYPE:Constants.Orientation.VERTICAL,Parameters.Completion.IPRMODEL:Constants.IPRModels.IPRPIMODEL,Parameters.Completion.RESERVOIRPRESSURE:A.reservoir_pressure,Parameters.IPRPIModel.LIQUIDPI:C,Parameters.IPRPIModel.USEVOGELBELOWBUBBLEPOINT:False,Parameters.Completion.RESERVOIRTEMPERATURE:A.reservoir_temperature,Parameters.Well.ASSOCIATEDBLACKOILFLUID:'wellfluid'})
		except:A.model.set_value(context=B,parameter=Parameters.Completion.TOPMEASUREDDEPTH,value=A.perforation_depth);A.model.set_value(context=B,parameter=Parameters.Completion.RESERVOIRPRESSURE,value=A.reservoir_pressure);A.model.set_value(context=B,parameter=Parameters.IPRPIModel.LIQUIDPI,value=C);A.model.set_value(context=B,parameter=Parameters.Completion.RESERVOIRTEMPERATURE,value=A.reservoir_temperature)
		logger.info('IPR created with reservoir conditions and fluid properties.');A.model.save()
	except:logger.error('Unable to creater the desired IPR.')