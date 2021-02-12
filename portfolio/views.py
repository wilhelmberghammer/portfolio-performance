import requests
import os 
from django.shortcuts import render, reverse, redirect
from django.views import generic

from .models import Stock
from .forms import PositionForm, StockModelForm



def get_data(symbol, interval, start_date):
	'''
		* symbol ... stock symbol -> string
		* interval ... interval -> sting (1min, 5min, 15min, 30min, 45min, 1h, 2h, 4h, 8h, 1day, 1week, 1month)
		* start_date ... start date -> YYYY-MM-DD
	'''
	api_key = os.environ.get("TWELVE_DATA_API_KEY")


	response = requests.get(f"https://api.twelvedata.com/time_series?symbol={symbol}&interval={interval}&start_date={start_date}&apikey={api_key}")



def portfolio_list(request):
	stocks = Stock.objects.all()


	context = {
		"stocks": stocks
	}
	return render(request, "portfolio/portfolio_list.html", context)


class PositionCreateView(generic.CreateView):
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