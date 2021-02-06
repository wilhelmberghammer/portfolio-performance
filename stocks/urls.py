from django.urls import path

from .views import stock

app_name = 'stocks'

urlpatterns = [
	path('', stock, name='lead-list'),
]