from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Restaurant(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    logo = models.ImageField(upload_to='restaurant_logos', null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
   		 return reverse("restaurant-detail", kwargs={"restaurant_id": self.id})

    def __str__(self):
    	return self.name

class Item(models.Model):
	name = models.CharField(max_length=20)
	description = models.TextField()
	price = models.FloatField()
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

	def get_absolute_url(self):
   		 return reverse("restaurant-detail", kwargs={"restaurant_id": self.id})
