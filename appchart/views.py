#from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response

#User = get_user_model()

class HomeView(View):
   def get(self, request, *args, **kwargs):        
        return render(request, 'charts.html', {"customers": 10})
        



def get_data(request, *args, **kwargs):       
    data ={
        "sales":100,
        "customers": 10,        
    } 
    return JsonResponse(data)

class ChartData(APIView):    
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        data ={
            "sales":100,
            "customers": 10,
            "users": ["michael", "tina", "albert"],
            #"users": User.objects.all().count(),        
        }        
        return Response(data)