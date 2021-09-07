from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from .serializers import User_Serializer
from .models import User

# Create your views here.

@api_view(['GET','POST','PUT','DELETE'])
@permission_classes([AllowAny,])
def User_View(request,pk=None):
      if request.method =='GET':
          id = request.data.get('id')
          if id is not None:
              user = User.objects.get(id=id)
              serializer = User_Serializer(user)
              return Response(serializer.data)
          paginator = PageNumberPagination()
          user = User.objects.all()
          paginator.page_size = 5
          result_page = paginator.paginate_queryset(user,request)
          serializer = User_Serializer(result_page,many=True)
          return paginator.get_paginated_response(serializer.data)

      if request.method == 'POST':
          serializer = User_Serializer(data=request.data)
          if serializer.is_valid():
              serializer.save()
              res = {'msg':'Data has been Created Successfully'}
              return Response(res,status=HTTP_201_CREATED)
          return Response(serializer.errors)


      if request.method =='PUT':
          id = request.data.get('id')
          user = User.objects.get(pk=id)
          serializer = User_Serializer(user,data=request.data)
          if serializer.is_valid():
              serializer.save()
              return Response({'msg':'Data Updated'})
          return Response(serializer.errors)

      if request.method =='PATCH':
          id = request.data.get('id')
          user = User.objects.get(pk=id)
          serializer = User_Serializer(user,data=request.data,partial=True)
          if serializer.is_valid():
              serializer.save()
              return Response({'msg':'Data Updated'})
          return Response(serializer.errors)

      if request.method == 'DELETE':
          id = request.data.get('id')
          user = User.objects.get(pk=id)
          user.delete()
          return Response({'msg':'Data Deleted'})

