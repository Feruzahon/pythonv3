from rest_framework.permissions import BasePermission#это родительский класс где заготовлена какаята логика 

class IsAuthorOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):#это раюбота с определенном обьектом
        if request.user.is_superuser or request.user.is_staff:#туту проверяется если есть активный пользователь или администратор может изменовать
            return True
        return obj.user == request.user#тут проверяем юзер обьекта если равно тому юзеру то можно изменить 
    #это функция работает когда работаем с обьектом поэтому используем has_object_permissions

#написать код '16.09.25'
