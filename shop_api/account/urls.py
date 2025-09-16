from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
#это вьюшка нужно для логина и оно создает токены оно нам нужны понять что что активирован ли пользователь

from .views import RegisrtUserView, ActivateView

urlpatterns = [
    path('register/',RegisrtUserView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('activate/', ActivateView.as_view())


]