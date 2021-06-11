from django.db import models

class PizzaModel(models.Model):
 	name = models.CharField(max_length = 10)
 	price = models.CharField(max_length = 10)

class CustomerModel(models.Model):
	userid = models.CharField(max_length = 10)
	phoneno = models.CharField(max_length = 10)

class OrderModel(models.Model):
	username = models.CharField()
	phoneno = models.CharField()
	address = models.CharField()
	ordereditems = models.CharField()
	status = models.CharField()


