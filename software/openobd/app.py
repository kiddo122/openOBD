"""Main app for openOBD"""

import sys
sys.path.append('../')

from config.iconfiguration import IConfiguration
from config.configuration import Configuration

from shell.shell import Shell

from gps.igpsdevice import IGPSDevice
from gps.gps3device import GPS3Device

from obd.iobddevice import IOBDDevice
from obd.obddevice import OBDDevice

from api.api import Api

from accelerometer.iacceldevice import IAccelDevice
from accelerometer.mpuacceldevice import MPUAccelDevice

from thermo.ithermodevice import IThermoDevice
from thermo.mputhermodevice import MPUThermoDevice

class App():
	def __init__(self):
		self.CONFIG_FILENAME = 'config/config.ini'
		self._config = None
		self._gpsDevice = None
		self._accelDevice = None
		self._thermoDevice = None
		self._api = None
		self._obdDevice = None
		self.read_configuration_file()
		self.configure_gps()
		self.configure_thermo()
		self.configure_acceleromenter()
		self.configure_api()
		self.configure_obd()
		self.configure_shell()

	def configure_api(self):
		self._api = Api()

	def configure_obd(self):
		self._obdDevice = OBDDevice()

	def read_configuration_file(self):
		self._config = Configuration()
		self._config.read(self.CONFIG_FILENAME)

	def configure_gps(self):
			self._gpsDevice = GPS3Device()

	def configure_acceleromenter(self):
			self._accelDevice = MPUAccelDevice()

	def configure_thermo(self):
			self._thermoDevice = MPUThermoDevice()

	def configure_shell(self):
		self._shell = Shell(self._gpsDevice, self._thermoDevice, self._accelDevice, self._api, self._obdDevice)


	def run(self):
		self._shell.cmdloop()

if __name__ == '__main__':
	app = App()
	app.run()
