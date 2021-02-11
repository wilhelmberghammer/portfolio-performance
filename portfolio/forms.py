from django import forms
from .models import Stock

class StockModelForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = (
			'symbol',
			'start_date',
			'amount',
		)

class PositionForm(forms.Form):
	symbol = forms.CharField()
	start_date = forms.CharField()
	amount = forms.IntegerField(min_value=1)
