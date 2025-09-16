from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.permissions import IsAuthenticatedOrReadOnly  #перемешены это то что дает ограничение на какие либо действий 
from rest_framework.viewsets import ModelViewSet
from .models import Product,Category
from .serializers import Productserializer,CateforySerializer
from .permissions import IsAuthorOrAdmin
from rest_framework.filters import SearchFilter


class ProductModelViewSet(ModelViewSet):#тут для создание , удаление, получение списка то есть все манипуляции сложены внутри его
    queryset = Product.objects.all()
    serializer_class = Productserializer
    filter_backends = [DjangoFilterBackend]#это филтирацияя джанго
    
    #по каким полям мы будем филтировать данные

    #permission_classes = [IsAuthenticatedOrReadOnly]#тут использовали стройную перемешену
    def get_permissions(self):
        if self.action in ['destroy','update','partial_update']:#
            return[IsAuthorOrAdmin()]
        else:
            return [IsAuthenticatedOrReadOnly()]


'16.09.25'
class CategoryModelView(ProductModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CateforySerializer
    permission_classes=[IsAuthenticatedOrReadOnly]
    ##
    filter_backends = [SearchFilter]
    search_fields = ['title']
