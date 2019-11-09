from django.shortcuts import render
from .models import dict_database
from django.http import HttpResponseRedirect

# Create your views here.


def post_index(request):
  
    origin = request.POST['origin']
    destination = request.POST['destination']
    print("orgin: "+origin+"\ndestination: "+ destination)

    return HttpResponseRedirect('/home/')

def get_index(request):
    return render(request, 'index.html')
