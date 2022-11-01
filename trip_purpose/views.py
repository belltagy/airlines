from django.shortcuts import render

from django.conf import settings
from amadeus import Client, ResponseError 
from django.contrib import messages 
AMADEUS_CLIENT_ID= getattr(settings,'AMADEUS_CLIENT_ID')
AMADEUS_CLIENT_SECRET=getattr(settings,'AMADEUS_CLIENT_SECRET')

amadeus = Client(client_id=AMADEUS_CLIENT_ID, 
                 client_secret=AMADEUS_CLIENT_SECRET, 
                 log_level='debug')
def prediction(request): 
    kwargs = {'originLocationCode': request.POST.get('Origin'), 
              'destinationLocationCode': request.POST.get('Destination'), 
              'departureDate': request.POST.get('Departuredate'), 
              'returnDate': request.POST.get('Returndate')} 
    try: 
        purpose = amadeus.travel.predictions.trip_purpose.get( 
            **kwargs).data['result'] 
    except ResponseError as error: 
        print("error>>>>>>>>>",error) 
        messages.add_message(request, messages.ERROR, error) 
        return render(request, 'trip_purpose/home.html', {}) 
    return render(request, 'trip_purpose/home.html', {'prediction': purpose}) 
