from src import Wifi, Hostapd, Stellar
import time
import signal
import sys

wifi = Wifi("coucou")
hostapd = Hostapd()
stellar = Stellar()

def sigint_handler(signal, frame):
	hostapd.stop()
	sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)

def loopStellar():
	lastPrice = 0.0
	while True:
		prices = stellar.gatherPrice()

		if lastPrice != prices['EUR']:
			print(prices['EUR'])
			wifi.SSID = 'Stellar Lumens - {} EUR'.format(prices['EUR'])
			config = wifi.generateConfig()

			hostapd.publishConfig(config)

			hostapd.restart()

			lastPrice = prices['EUR']
			time.sleep(1)

if __name__ == "__main__":
	loopStellar()