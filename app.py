#!/usr/bin/python

from src import Wifi, Hostapd, Stellar
import time
import signal
import argparse
import sys

wifi = Wifi("Stellar Lumens prices")
hostapd = Hostapd()
stellar = Stellar()

def sigint_handler(signal, frame):
	hostapd.stop()
	sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)

def loopStellar(args):
	currency = args.currency
	interval = args.interval

	lastPrice = 0.0
	while True:
		prices = stellar.gatherPrice(currency)

		if lastPrice != prices[currency]:
			print(prices[currency])
			wifi.SSID = 'Stellar Lumens - {} {}'.format(prices[currency], currency)
			config = wifi.generateConfig()

			hostapd.publishConfig(config)

			hostapd.restart()

			lastPrice = prices[currency]
		time.sleep(interval)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Stellar prices SSID')
	parser.add_argument('--currency', '-c', dest='currency', default='USD', help='Stellar price in selected currency')
	parser.add_argument('--interval', '-i', type=float, dest='interval', default=60, help='Update interval in seconds')

	args = parser.parse_args()

	loopStellar(args)