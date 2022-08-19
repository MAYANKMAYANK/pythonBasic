from django.shortcuts import render
from myapi import serializers
from . models import ADDDATA
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from .serializers import AlldataSerializer,adddataSerializer,upddataSerializer
from rest_framework import serializers

# Create your views here.


#read api
@api_view(['GET'])
def all_data(request):
    snippets = ADDDATA.objects.all()
    serializer = AlldataSerializer(snippets, many=True)
    # return JsonResponse(serializer.data, safe=False)
    return JsonResponse({"data":serializer.data,"message":"All data list","code":200}, safe=False)


#add pickup post api
@api_view(['POST'])
def add_data(request):
  if request.method == 'POST':
    serializer = adddataSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"success":"successfully"})
  print("*"*8)
  return Response({"success":"Bad request"})

#delete data api
@api_view(["DELETE"])
def delete_data(request,uid):
    ADDDATA.objects.get(id=uid).delete()
    return Response({"success":"delete successully"})
#    return JsonResponse(serializer.data, safe=False)



#update  put method api
@api_view(['PUT'])
def upd_data(request,uid):
  if request.method == 'PUT':
    snippet = ADDDATA.objects.get(id=uid)
    serializer=upddataSerializer(snippet, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"success":"updated successfully"})
    else:
      return Response({"success":"not updated successfully"})
