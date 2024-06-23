from django.shortcuts import render
# parsing data from the client
from rest_framework.parsers import JSONParser
# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt
# for sending response to the client
from django.http import HttpResponse, JsonResponse
# API definition for task
from .serializers import dailyTasksSerializer
# Task model
from .models import dailyTasks

# Create your views here.

#daily tasks handler
@csrf_exempt
def dailyTasksAdd(request):
    if(request.method == 'GET'):
        dailytasks = dailyTasks.objects.all().order_by('dailyTaskStatus', 'dailyTaskPriority', 'dailyStartTime', 'dailyEndTime').values()
        serializer = dailyTasksSerializer(dailytasks, many=True)
        return JsonResponse(serializer.data,safe=False)
    elif(request.method == 'POST'):
        data = JSONParser().parse(request)
        serializer = dailyTasksSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt
def dailyTasksEdit(request, pk):
    try:
        dailytasks = dailyTasks.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)  
    if(request.method == 'PUT'):
        data = JSONParser().parse(request)  
        serializer = dailyTasksSerializer(dailytasks, data=data)
        if(serializer.is_valid()):  
            serializer.save() 
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif(request.method == 'DELETE'):
        dailytasks.delete() 
        return HttpResponse(status=204) 