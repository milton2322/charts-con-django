from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response



class HomeView(View):
   def get(self, request, *args, **kwargs):        
        return render(request, 'charts.html', {"customers": 10})
        



def get_data(request, *args, **kwargs): 
    labels = ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'] 
    default_items = [40,24,34,99,34,57]     
    data ={
        "labels":labels,
        "default": default_items, 
               
    } 
    return JsonResponse(data)

class ChartData(APIView):    
    authentication_classes = []
    permission_classes = []
    def get(self,request, format=None):
        labels = ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
        data ={
            "labels": 40,
            "customers": 10,     
        }        
        return Response(data)