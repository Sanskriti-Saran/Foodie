from django.shortcuts import render, get_object_or_404
from .models import FoodSpot

def home(request):
	"""
	Displays a list of all food spots, with search and filter support.
	"""
	q = request.GET.get('q', '')
	location = request.GET.get('location', '')
	min_price = request.GET.get('min_price', '')
	max_price = request.GET.get('max_price', '')
	food_spots = FoodSpot.objects.all()
	if q:
		food_spots = food_spots.filter(name__icontains=q)
	if location:
		food_spots = food_spots.filter(location__icontains=location)
	if min_price:
		food_spots = food_spots.filter(price__gte=min_price)
	if max_price:
		food_spots = food_spots.filter(price__lte=max_price)
	context = {
		'food_spots': food_spots,
		'page_title': 'All Famous Food Spots in Lucknow',
		'heading': 'Explore Lucknow\'s Culinary Royalty',
		'subheading': 'From Kebabs to Kulfi, a Taste of Awadhi Grandeur',
		'search_query': q,
		'location_query': location,
		'min_price': min_price,
		'max_price': max_price,
	}
	return render(request, 'home.html', context)

# def food_spot_detail(request, pk):
# 	"""
# 	Displays details of a single food spot.
# 	"""
# 	food_spot = get_object_or_404(FoodSpot, pk=pk)
# 	context = {
# 		'food_spot': food_spot,
# 		'page_title': f'{food_spot.name} - Lucknow Foodie',
# 	}
# 	return render(request, 'food_spot_detail.html', context)

def veg_spots(request):
	"""
	Displays a list of vegetarian food spots, with search and filter support.
	"""
	q = request.GET.get('q', '')
	location = request.GET.get('location', '')
	min_price = request.GET.get('min_price', '')
	max_price = request.GET.get('max_price', '')
	veg_food_spots = FoodSpot.objects.filter(food_type__in=['veg', 'both'])
	if q:
		veg_food_spots = veg_food_spots.filter(name__icontains=q)
	if location:
		veg_food_spots = veg_food_spots.filter(location__icontains=location)
	if min_price:
		veg_food_spots = veg_food_spots.filter(price__gte=min_price)
	if max_price:
		veg_food_spots = veg_food_spots.filter(price__lte=max_price)
	context = {
		'food_spots': veg_food_spots,
		'page_title': 'Vegetarian Delights of Lucknow',
		'heading': 'Pure Vegetarian Flavors',
		'subheading': 'A Rich Tapestry of Meat-Free Awadhi Cuisine',
		'search_query': q,
		'location_query': location,
		'min_price': min_price,
		'max_price': max_price,
	}
	return render(request, 'veg.html', context)

def non_veg_spots(request):
	"""
	Displays a list of non-vegetarian food spots, with search and filter support.
	"""
	q = request.GET.get('q', '')
	location = request.GET.get('location', '')
	min_price = request.GET.get('min_price', '')
	max_price = request.GET.get('max_price', '')
	non_veg_food_spots = FoodSpot.objects.filter(food_type__in=['non_veg', 'both'])
	if q:
		non_veg_food_spots = non_veg_food_spots.filter(name__icontains=q)
	if location:
		non_veg_food_spots = non_veg_food_spots.filter(location__icontains=location)
	if min_price:
		non_veg_food_spots = non_veg_food_spots.filter(price__gte=min_price)
	if max_price:
		non_veg_food_spots = non_veg_food_spots.filter(price__lte=max_price)
	context = {
		'food_spots': non_veg_food_spots,
		'page_title': 'Non-Vegetarian Extravaganza',
		'heading': 'The Grandeur of Non-Vegetarian Awadhi Cuisine',
		'subheading': 'Kebabs, Kormas, and More: A Royal Feast',
		'search_query': q,
		'location_query': location,
		'min_price': min_price,
		'max_price': max_price,
	}
	return render(request, 'nonveg.html', context)

def dessert_spots(request):
	"""
	Displays a list of dessert spots, with search and filter support.
	"""
	q = request.GET.get('q', '')
	location = request.GET.get('location', '')
	min_price = request.GET.get('min_price', '')
	max_price = request.GET.get('max_price', '')
	dessert_food_spots = FoodSpot.objects.filter(category='dessert')
	if q:
		dessert_food_spots = dessert_food_spots.filter(name__icontains=q)
	if location:
		dessert_food_spots = dessert_food_spots.filter(location__icontains=location)
	if min_price:
		dessert_food_spots = dessert_food_spots.filter(price__gte=min_price)
	if max_price:
		dessert_food_spots = dessert_food_spots.filter(price__lte=max_price)
	context = {
		'food_spots': dessert_food_spots,
		'page_title': 'Sweet Endings: Lucknow Desserts',
		'heading': 'Indulge in Awadhi Sweets',
		'subheading': 'A Symphony of Flavors to Conclude Your Royal Meal',
		'search_query': q,
		'location_query': location,
		'min_price': min_price,
		'max_price': max_price,
	}
	return render(request, 'desserts.html', context)

def full_course_spots(request):
	"""
	Displays a list of full course meal spots, with search and filter support.
	"""
	q = request.GET.get('q', '')
	location = request.GET.get('location', '')
	min_price = request.GET.get('min_price', '')
	max_price = request.GET.get('max_price', '')
	full_course_food_spots = FoodSpot.objects.filter(category='full_course')
	if q:
		full_course_food_spots = full_course_food_spots.filter(name__icontains=q)
	if location:
		full_course_food_spots = full_course_food_spots.filter(location__icontains=location)
	if min_price:
		full_course_food_spots = full_course_food_spots.filter(price__gte=min_price)
	if max_price:
		full_course_food_spots = full_course_food_spots.filter(price__lte=max_price)
	context = {
		'food_spots': full_course_food_spots,
		'page_title': 'Full Course Meals: Lucknow',
		'heading': 'Grand Awadhi Full Course Meals',
		'subheading': 'Savor the Richness of Lucknowi Dastarkhwan',
		'search_query': q,
		'location_query': location,
		'min_price': min_price,
		'max_price': max_price,
	}
	return render(request, 'meals.html', context)
