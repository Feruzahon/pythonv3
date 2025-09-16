from django.db import models

from account.models import CustomUser




class Category(models.Model):#это категории товаров 
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    prise = models.PositiveIntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category,on_delete = models.CASCADE,related_name='products')
    user = models.ForeignKey(CustomUser, on_delete= models.CASCADE, related_name='products',blank =True)# если нас пользователь удалитса то его продукты тоже удалится за счет CASCADE

    def __str__(self):
        return self.title
    