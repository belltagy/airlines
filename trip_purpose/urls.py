from django.urls import path 
from . import views 
app_name="trip_purpose"
urlpatterns = [ 
    path('', views.prediction, name='prediction'), 
] 