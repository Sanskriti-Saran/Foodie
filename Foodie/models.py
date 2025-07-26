from django.db import models

class FoodSpot(models.Model):
	FOOD_TYPE_CHOICES = [
		('veg', 'Vegetarian'),
		('non_veg', 'Non-Vegetarian'),
		('both', 'Both'),
	]
	CATEGORY_CHOICES = [
		('dessert', 'Dessert'),
		('full_course', 'Full Course'),
		('other', 'Other'),
	]
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	address = models.CharField(max_length=255, blank=True)
	location = models.CharField(max_length=100, blank=True)
	price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
	food_type = models.CharField(max_length=10, choices=FOOD_TYPE_CHOICES)
	category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
	image = models.URLField(blank=True)

	def __str__(self):
		return self.name
