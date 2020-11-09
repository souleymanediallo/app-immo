from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor


# Create your views here.
def home(request):
    listings = Listing.objects.all()[:3]
    context = {'listings': listings}
    return render(request, "pages/index.html", context)


def about(request):
    return render(request, "pages/about.html")