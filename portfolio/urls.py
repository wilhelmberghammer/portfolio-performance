from django.urls import path

from .views import portfolio_list, PositionCreateView, PositionEditView, PositionDeleteView 

app_name = 'portfolio'

urlpatterns = [
	path('', portfolio_list, name='portfolio-list'),
	path('new/', PositionCreateView.as_view(), name='new-position'),
	path('<int:pk>/edit', PositionEditView.as_view(), name='position-edit'),
	path('<int:pk>/delete', PositionDeleteView.as_view(), name='position-delete'),
]