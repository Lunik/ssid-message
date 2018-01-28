import random
import string
import re

WLAN_IFACE = 'wlan0'

class Wifi:
	def __init__(self, SSID):
		self.SSID = SSID
		pass

	def generateConfig(self):
		config = '''interface={}
			driver=nl80211
			ssid={}
			hw_mode=g
			channel={}
			wmm_enabled=0
			macaddr_acl=0
			auth_algs=1
			ignore_broadcast_ssid=0
			wpa=2
			wpa_passphrase={}
			wpa_key_mgmt=WPA-PSK
			wpa_pairwise=TKIP
			rsn_pairwise=CCMP'''.format(WLAN_IFACE,
			self.SSID,
			random.randint(0, 9),
			''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(50))
			)

		return re.sub('\t', '', config)