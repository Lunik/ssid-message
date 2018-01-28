import requests

class Stellar:
	def __init__(self):
		pass

	def gatherPrice(self, currency):
		# https://min-api.cryptocompare.com/data/price?fsym=XLM&tsyms=XLM,USD,EUR
		response = requests.get('https://min-api.cryptocompare.com/data/price?fsym=XLM&tsyms=XLM,{}'.format(currency))

		return response.json()