from django.shortcuts import render

from listings.choices import price_choices, bedroom_choices, state_choices
from listings.models import Listing
from realtors.models import Realtor


# Create your views here.
def home(request):
    listings = Listing.objects.all()[:3]
    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }
    return render(request, "pages/index.html", context)


def about(request):
    realtors = Realtor.objects.all()
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {'realtors': realtors, 'mvp_realtors': mvp_realtors}
    return render(request, "pages/about.html", context)


def search(request):
    queryset_list = Listing.objects.all()[:3]

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = Listing.objects.filter(description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = Listing.objects.filter(city__iexact=city)

    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = Listing.objects.filter(city__iexact=state)

    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = Listing.objects.filter(bedrooms__iexact=bedrooms)

    # Bedrooms
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = Listing.objects.filter(price__lte=price)

    context = {
        'listings': queryset_list,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'values': request.GET,
    }
    return render(request, "pages/search.html", context)