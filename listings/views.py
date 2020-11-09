from django.shortcuts import render
from .models import Listing
from realtors.models import Realtor


# Create your views here.
def listing_list(request):
    listings = Listing.objects.all()
    context = {'listings': listings}
    return render(request, "listings/listing_list.html", context)