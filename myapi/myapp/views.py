from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import *
from .serializer import *
# Create your views here.

class todoapi(APIView):
    def get(self,request):
        tododata = todo.objects.all()
        todoser = todoserializer(tododata,many=True)
        return Response({"data":todoser.data})
    
    def post(self,request):

        ser_data =  todoserializer(data=request.data)
       
        if not ser_data.is_valid():
          return Response({"message":"something went wrong","errors":ser_data.errors})
        ser_data.save()
        return Response({"userdata":ser_data.data,"message":"todo inserted"})
    
    def put(self,request):
        try:
            id=request.data["id"]
            tododata =  todo.objects.get(id=id)
            ser_data = todoserializer(tododata,request.data)
            if not ser_data.is_valid():
              return Response({"message":"something went wrong","errors":ser_data.errors})
            ser_data.save()
            return Response({"userdata":ser_data.data,"message":"todo updated"})
        except Exception as e:
            print(e)
            return Response({"msg":"id not fond"})
        
    def delete(self,request):
        try:
            id=request.data["id"]
            tododata =  todo.objects.get(id=id)
            tododata.delete()
            
        except Exception as e:
            print(e)
            return Response({"msg":"id not fond"})