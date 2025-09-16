#импортируем библиотеку для стериализации- это перевод с одного на другую
# десирелизация это обратное процец именно это библиотека как раз помогает для этого, валидирует тоесть проверяет тодже на типы дынных
from rest_framework.serializers import ModelSerializer

#импортируем одноуровневое модули post
from .models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        
