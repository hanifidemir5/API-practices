from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view 
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer,MenuItemSerializer2
from django.shortcuts import get_object_or_404
# Create your views here.

@api_view(['GET','POST'])
def books(request):
    return Response('list of the books',status=status.HTTP_200_OK)

@api_view()
def menu_items(request):
    items = MenuItem.objects.all()
    serializer_item = MenuItemSerializer2(items,many=True)
    return Response(serializer_item.data)

@api_view()
def single_item(request, id):
    item = get_object_or_404(MenuItem,pk=id)
    serialized_item = MenuItemSerializer2(item)
    return Response(serialized_item.data)

class BookList(APIView):
    def get(self,request):
        author = request.GET.get('author')
        if (author):
            return Response({"message":"list of books by:" + author},status.HTTP_200_OK)
        
        return Response({"message":"list of the books"},status.HTTP_200_OK)
    def post(self,request):
        return Response({"title":request.data.get('title')},status.HTTP_201_CREATED)

class Book(APIView):
    def get(self,request,pk):
        return Response({"messsage":"single book with id: " + str(pk)},status.HTTP_200_OK)
    def put(self,request,pk):
        return Response({"title":request.data.get('title')},status.HTTP_200_OK)
    
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all() 
    serializer_class = MenuItemSerializer   
class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer    
    