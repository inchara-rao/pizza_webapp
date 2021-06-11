from django.db import models

class PizzaModel(models.Model):
 	name = models.CharField(max_length = 10)
 	price = models.CharField(max_length = 10)

class CustomerModel(models.Model):
	userid = models.CharField(max_length = 10)
	phoneno = models.CharField(max_length = 10)

class OrderModel(models.Model):
	username = models.CharField(max_length=255)
	phoneno = models.CharField(max_length=255)
	address = models.CharField(max_length=255)
	ordereditems = models.CharField(max_length=255)
	status = models.CharField(max_length=255)


