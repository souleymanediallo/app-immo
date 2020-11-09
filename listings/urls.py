from django.urls import path
from . import views

urlpatterns = [
    path('', views.listing_list, name="listing-list"),
    path('<int:listing_id>', views.listing_detail, name="listing-detail"),
]