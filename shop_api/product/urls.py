from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import ProductModelViewSet,CategoryModelView

roulter = DefaultRouter()
roulter.register('product', ProductModelViewSet)
roulter.register('category', CategoryModelView)

urlpatterns =[
    path('',include(roulter.urls))
    #так как мы используем модул теперь изпользуем ролтеры
]