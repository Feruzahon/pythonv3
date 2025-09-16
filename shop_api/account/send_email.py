from django.core.mail import send_mail

from decouple import config


HOST = config('HOST_FOR_SEND_MAIL')#нужно для перехода из ссылки на почте

def send_activation_email(email, activation_code):
    activation_url = f'{HOST}/account/activate/?u={activation_code}'
    message = ""
    html = f""" 
<h1>Для активации нажмите кнопку</h1>
<a href = "{activation_code}">
<button> Нажми сюда </button>
</a>

"""
    send_mail(
        subject = 'Активация аккаунта',
        message= message,
        from_email= "a@mail.com",
        recipient_list=[email],
        html_message=html
    )