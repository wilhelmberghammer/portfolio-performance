import requests
import os 
from django.shortcuts import render, reverse, redirect
from django.views import generic

from .models import Stock
from .forms import PositionForm, StockModelForm




def portfolio_list(request):
	stocks = Stock.objects.all()

	context = {
		"stocks": stocks
	}
	return render(request, "portfolio/portfolio_list.html", context)



def PositionDetailView(request, pk):
	api_key = os.environ.get("TWELVE_DATA_API_KEY")
	position = Stock.objects.get(id=pk)


	symbol = position.symbol
	interval = "1day"
	start_date = position.start_date
	amount = position.amount

	# get data
	response = requests.get(f"https://api.twelvedata.com/time_series?symbol={symbol}&interval={interval}&dp=2&start_date={start_date}&apikey={api_key}")
	resp = response.json()
	
	# extract values into list
	closing_list = []
	date_list = []

	for i in range(len(resp['values'])):
		closing_list.append(float(resp['values'][i]['close']))
		date_list.append(resp['values'][i]['datetime'])

	closing_list.reverse()
	date_list.reverse()

	# data that needs to be passed
	currency = resp['meta']['currency']
	exchange = resp['meta']['exchange']

	last_closing_price = round(closing_list[-1], 2)
	change_pct = round((closing_list[-1]/closing_list[0]-1)*100, 2)
	current_position_value = last_closing_price*amount

	
	if change_pct < 0:
		change_color = 'text-red-500' 
	elif change_pct > 0:
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
		'current_position_value': current_position_value,
		'change_color': change_color,
	}	
	return render(request, "portfolio/detail_position.html", context)




class PositionCreateView(generic.CreateView):
	'''
	TODO:
		* after positions has be created -> Review Position -> call API (display info) -> confirm/delete
	'''
	template_name = 'portfolio/new_position.html'
	form_class = StockModelForm
	
	def get_success_url(self):
		return reverse("portfolio:portfolio-list")


class PositionEditView(generic.UpdateView):
	template_name = 'portfolio/edit_position.html'
	queryset = Stock.objects.all()
	form_class = StockModelForm
	
	def get_success_url(self):
		return reverse("portfolio:portfolio-list")


class PositionDeleteView(generic.DeleteView):
	template_name = 'portfolio/delete_position.html'
	queryset = Stock.objects.all()
	
	def get_success_url(self):
		return reverse("portfolio:portfolio-list")  