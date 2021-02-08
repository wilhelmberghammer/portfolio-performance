from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	pass


class Stock(models.Model):
	symbol = models.CharField(max_length=10)
	start_date = models.CharField(max_length=20) 	# example: 2020-03-23 09:00:00
	amount = models.IntegerField(default=1)

	def __str__(self):
		return f'{self.symbol}, bought {self.amount} shares on {self.start_date}'
