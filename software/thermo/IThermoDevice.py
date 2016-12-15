import abc

class IThermometerDevice(abc.ABC):

	@abc.abstractmethod
	def initialize() :
		return

	# check that the device is available and able to provide temperature measurements
	@abc.abstractmethod
	def getStatus() :
		return
		
	# create a new ITemperature
	@abc.abstractmethod
	def getTemperature() :
		return