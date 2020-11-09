from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Listing
from realtors.models import Realtor


# Create your views here.
def listing_list(request):
    listings = Listing.objects.all()

    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {'listings': paged_listings}
    return render(request, "listings/listing_list.html", context)


def listing_detail(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {'listing': listing}
    return render(request, "listings/listing_detail.html", context)