from rest_framework.serializers import ModelSerializer

from .models import Product,Category

class CateforySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


#надо писать перемешены в это время читала намаз


class Productserializer(ModelSerializer): 
    class Meta:#указываем этот класс для волидатсии в классе указывваем vievs 
        model = Product
        fields = '__all__'

    def to_representstion(self, instance):#это отображение по категории
        repr =- super().to_representation(instance)
            #category = Category.objects.get(id = instance.category.id)
        repr['category'] = CateforySerializer(instance =instance.category).data
        return repr#мы тут переименовали и место число название категории то есть обьект

    def create(self, validated_data):
        validated_data['user'] = self.context.get('request').user
        return super().create(validated_data)