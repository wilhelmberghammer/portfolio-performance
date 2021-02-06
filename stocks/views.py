import requests
from django.shortcuts import render
from django.views import generic
import os 


def stock(request):
	'''
		Testing - that's why it looks so bad
	'''


	api_key = os.environ.get("TWELVE_DATA_API_KEY")

	symbol="NVDA"
	interval = "1day"
	outputsize = 30
	start_date = "2021-01-01 19:19:00" 

	response = requests.get(f"https://api.twelvedata.com/time_series?symbol={symbol}&interval={interval}&start_date={start_date}&apikey={api_key}")

	resp = response.json()
	
	closing_list = []
	date_list = []

	for i in range(24):
		closing_list.append(float(resp['values'][i]['close']))
		date_list.append(resp['values'][i]['datetime'])

	closing_list.reverse()
	date_list.reverse()

	symbol = resp['meta']['symbol']
	currency = resp['meta']['currency']
	exchange = resp['meta']['exchange']

	context = {
		'closing_list': closing_list,
		'date_list': date_list,
		'symbol': symbol,
		'currency': currency,
		'exchange': exchange,
	}

	return render(request, 'stocks/stock.html', context)