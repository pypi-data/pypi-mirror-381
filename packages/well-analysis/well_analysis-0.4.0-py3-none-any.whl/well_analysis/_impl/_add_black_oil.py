from._logger import logger
from sixgill.definitions import ModelComponents,Parameters
def add_black_oil(self,q_gas,q_oil,q_water,api,gg,gas_well=False):
	E=q_water;D=q_gas;C='wellfluid';B=q_oil;A=self
	try:
		A.q_gas=D;A.q_water=E
		if B==0:F=9.99*10**9/35.4*6.29;B=D/F;A.q_oil=B
		else:A.q_oil=B
		A.gas_well=gas_well;A.api=api;A.gg=gg;A.gor=D/B;A.wc=E/(E+B)*100
		try:A.model.add(ModelComponents.BLACKOILFLUID,C,parameters={Parameters.BlackOilFluid.GOR:A.gor,Parameters.BlackOilFluid.WATERCUT:A.wc,Parameters.BlackOilFluid.API:A.api,Parameters.BlackOilFluid.GASSPECIFICGRAVITY:A.gg});A.model.set_value(Well='main_well',parameter=Parameters.Well.ASSOCIATEDBLACKOILFLUID,value=C)
		except:A.model.set_value(context=C,parameter=Parameters.BlackOilFluid.GOR,value=A.gor);A.model.set_value(context=C,parameter=Parameters.BlackOilFluid.WATERCUT,value=A.wc);A.model.set_value(context=C,parameter=Parameters.BlackOilFluid.API,value=A.api);A.model.set_value(context=C,parameter=Parameters.BlackOilFluid.GASSPECIFICGRAVITY,value=A.gg)
		A.model.save();logger.info('Black oil fluid added to the model.')
	except:logger.error('Unable to add the black oil properties.')