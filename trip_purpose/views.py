from django.shortcuts import render

def prediction(request): 
    return render(request, 'trip_purpose/home.html', {}) 