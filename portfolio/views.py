'''
TODO:
	* portfolio_list
		* calculate ytd performance and pass to frontend
		* calculate overall performance and pass to frontend
		* graph performance
	* portfolio_detail
		* calculate ytd performance
		* calculate overall performance
		* graph performance
	* add position
'''

import requests
import os 
from django.shortcuts import render
from django.views import generic

from .models import Stock


def get_data(symbols, interval, start_date):
	'''
		* symbols ... stock symbols -> list
		* interval ... interval -> sting (1min, 5min, 15min, 30min, 45min, 1h, 2h, 4h, 8h, 1day, 1week, 1month)
		* start_date ... start date -> YYYY-MM-DD
	'''
	api_key = os.environ.get("TWELVE_DATA_API_KEY")


	requests = response = requests.get(f"https://api.twelvedata.com/time_series?symbol={symbols}&interval={interval}&start_date={start_date}&apikey={api_key}")


def portfolio_list(request):
	stocks = Stock.objects.all()




	context = {
		"stocks": stocks
	}
	return render(request, "portfolio/portfolio_list.html", context)
