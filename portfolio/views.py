from django.shortcuts import render

def portfolio_list(request):
	text = 'protfolio list'

	context = {
		'text': text,
	}
	return render(request, 'portfolio/portfolio_list.html', context)
