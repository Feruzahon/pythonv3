from django.contrib.auth.base_user import BaseUserManager
from .send_email import send_activation_email

class UserManager(BaseUserManager):
    def create_user(self, email,password,**extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)#строенная функция для проверки 
        user = self.model(email = email, **extra_fields)
        user.set_password(password)#захошировали пароль именно в этом части стобы в база данных сохранился в другом виде 
        user.create_activation_code()#вызвали функцию
        send_activation_email(user.email, user.activation_code)
        user.save(using = self._db)
        return user
    
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)#метод словарей и это означает он имеет много привелигие
        extra_fields.setdefault('is_active',True)#это поле чтобы активировать акаунт 
        extra_fields.setdefault('is_superuser',True)#это поле 
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)#
        user.set_password(password)
        user.save(using = self._db)
        return user 



    #у нас есть менежер , создаюм функцию для добавление пользователя , если при заполнение он не указал имеил то отправляем сообщение про это
    
    #менежер - это помошник который заимодействует с оремкой . з
    # десь мы выносим свою логику, так как отправка сылки для 
    # активации небыло бы 
    #