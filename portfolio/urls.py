from django.urls import path

from .views import portfolio_list, PositionCreateView

app_name = 'portfolio'

urlpatterns = [
	path('', portfolio_list, name='portfolio-list'),
	path('new/', PositionCreateView.as_view(), name='new-position'),
]