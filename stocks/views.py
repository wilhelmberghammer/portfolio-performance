import requests
from django.shortcuts import render
from django.views import generic
import os 


def stock(request):
	'''
		Testing - that's why it looks so bad
	'''


	api_key = os.environ.get("TWELVE_DATA_API_KEY")

	symbol="GME"
	interval = "1day"
	outputsize = 30
	start_date = "2020-01-01 00:00:00" 

	response = requests.get(f"https://api.twelvedata.com/time_series?symbol={symbol}&interval={interval}&start_date={start_date}&apikey={api_key}")
	resp = response.json()
	
	closing_list = []
	date_list = []

	for i in range(len(resp['values'])):
		closing_list.append(float(resp['values'][i]['close']))
		date_list.append(resp['values'][i]['datetime'])

	closing_list.reverse()
	date_list.reverse()


	symbol = resp['meta']['symbol']
	currency = resp['meta']['currency']
	exchange = resp['meta']['exchange']
	last_closing_price = round(closing_list[-1], 2)
	change_pct = round((closing_list[-1]/closing_list[0]-1)*100, 2)

	
	color = 'rgb(255, 140, 0)'
	if change_pct < 0:
		change_color = 'text-red-500' 

	if change_pct > 0:
		change_color = 'text-green-600'
	else:
		change_color = 'text-gray-900'


	context = {
		'closing_list': closing_list,
		'date_list': date_list,
		'symbol': symbol,
		'currency': currency,
		'exchange': exchange,
		'change_pct': change_pct,
		'last_closing_price': last_closing_price,
		'change_color': change_color,
	}

	return render(request, 'stocks/stock.html', context)