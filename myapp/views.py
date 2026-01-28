from django.shortcuts import render

from rest_framework.views import APIView 
from rest_framework.response import Response
from .models import CocaCola
from .serializer import CocaColaSerializer
class CocaColaApiView(APIView):
    def get(self, request, pk=None):
        print(pk)
        if pk:
            try:
                cocacola = CocaCola.objects.get(id=pk)
                ser = CocaColaSerializer(cocacola)
            except:
                return Response({
                    "message": "market not found"
                })
        else:
            cocacolas = CocaCola.objects.all()
            ser = CocaColaSerializer(cocacolas, many=True)
        return Response(ser.data)
    
    def post(self, request,pk=None):
        data = CocaColaSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(data.errors)
    def put(self, request, pk=None):
        if  pk:
            data=CocaCola.objects.filter(id=pk).first()
            data=CocaColaSerializer(data, data=request.data)
            if data.is_valid():
                data.save()
                return Response({'message':' market updated',
                                 'ser':data.data})
        else:
            return Response({'message':' market not found'})
        return Response(data.errors)
    
    def delete(self,request,pk=None):
                try:
                   cocacola=CocaCola.objects.get(id=pk)
                   cocacola.delete()
                   msg='market deleted successfully'
                except:
                    msg='market  not found'
                    return Response({'message':msg})