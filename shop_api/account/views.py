from django.shortcuts import render
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404,redirect

from rest_framework.response import Response
from .models import CustomUser

from .serializers import RegisterSerializer#э
#надо дополнить потом еще занова пройти  ./manage.py makemigratio'--4.08.25 ---'
class RegisrtUserView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response('Вы успешно зарегистрировались',status=201)



class ActivateView(APIView):
    def get(self, request):
        activation_code = request.query_params.get('u')
        user = get_object_or_404(CustomUser, activation_code = activation_code)
        user.is_active = True
        user.activation_code =''
        user.save()
        return redirect('https://google.com')#открытие страницы означает этот метод 

#redirect - это страница входы на сайт получается эту часть изменяется 
# когда франтеншик добавить гласную страницу длы входа