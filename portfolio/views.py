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
'''


from django.shortcuts import render

from .models import Stock


def portfolio_list(request):
	stocks = Stock.objects.all()

	context = {
		"stocks": stocks
	}
	return render(request, "portfolio/portfolio_list.html", context)
