from django.shortcuts import render
from .models import dict_database
from django.http import HttpResponseRedirect
from home.getRoute import getAddresses, getRoute, getDirections
import googlemaps
from datetime import datetime


gmaps = googlemaps.Client(key='AIzaSyB2UYBQZJIIb4bIHYnw858xSM6QWwj5CbI')

# Create your views here.


def post_index(request):
    
    origin = request.POST['origin']
    destination = request.POST['destination']
    ad = getAddresses(origin, destination)
    now = datetime.now()
    
    print(getDirections(ad))
    
    return HttpResponseRedirect('/home/')

def get_index(request):
    return render(request, 'index.html')
