import subprocess

class Hostapd:
	def __init__(self):
		self.CONFIG_PATH = '/etc/hostapd/hostapd.conf'

	def publishConfig(self, config):
		file = open(self.CONFIG_PATH,'w') 
		file.write(config)
		file.close()

	def restart(self):
		subprocess.call(["systemctl", "restart", "hostapd"])

	def stop(self):
		subprocess.call(["systemctl", "stop", "hostapd"])
