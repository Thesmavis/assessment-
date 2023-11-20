from functools import partial
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import *
from . serializers import *
# Create your views here.

class candidateview(APIView):
    def get(self, request, id = None):

        if id:
            try:
                get_data=Candidatedirectory.objects.get(id=id)
                data1=candidate_ser(get_data)
                return Response(data1.data)
            except:
                get_data=Candidatedirectory.objects.all()
                data1=candidate_ser(get_data)
                return Response(data1.data)
        else:
            get_data=Candidatedirectory.objects.all()
            data1=candidate_ser(get_data)
            return Response(data1.data)
    def post(self,request):
        serializer=candidate_ser(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(status=status.HTTP_201_CREATED)
        else:
            serializer.errors
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,id=None):
        if id:
            data2=Candidatedirectory.objects.get(id=id)
            serializer=candidate_ser(data2,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            else:
                serializer.errors
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id=None):
        try:
                get_data=Candidatedirectory.objects.get(id=id)
                get_data.delete()
                return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)