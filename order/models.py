from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	description = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

class Order(models.Model):
	customer_name =  models.CharField(max_length=200,null='True')
	phone = models.CharField(max_length=200,null='True')
	address = models.CharField(max_length=500,null='True')
	product_name = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True)
	payment_option =models.CharField(max_length=200,null='True')
	
	
	def __str__(self):
		return self.product_name.name

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=200,null=True)
	image = models.ImageField(default='default.png',upload_to='profile_pics')

	def __str__(self):
		return self.user.username