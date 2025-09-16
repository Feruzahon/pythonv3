from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.viewsets import ViewSet,ModelViewSet


from .serializers import PostSerializer
from .models import Post



'---28.08.25--'

'--2--'
#это основной логика и простое то есть базовые 
class PostModelViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

'--1--'
#class PostViewSet(ViewSet):
#    queryset = Post.objects.all()

#    def list(self,request):
#        queryset = Post.objects.all()
#        serializer = PostSerializer(queryset, many = True)
 #       return Response(serializer.data)


#    def retrieve(self,request, pk=None):
 #       post = get_object_or_404(Post,id=pk)
 #       serializer = PostSerializer(post)
  #      return Response(serializer.data)
    


        

#class ListCreatePostAPIiew(generics.ListCreateAPIView):
 #   queryset = Post.objects.all()
  #  serializer_class=PostSerializer    

'class Ret-дописать надо'
#class RetrievUpdateDestrovPostAPView(generics.RetrieveDestroyAPIView):
 #   queryset = Post.objects.all()
  #  serializer_class=PostSerializer 
# Create your views here.



'сегодня написали женериксы'


##вьющка для создании готова
#class CreatePostAPIView(generics.CreateAPIView):
 #   serializer_class = PostSerializer

#класс на гет
#class PostListApiiew(generics.ListAPIView):
 #   queryset = Post.objects.all()
 #   serializer_class = PostSerializer
    #это класс нам будет помогать получить данные то есть посты

#
#class PostRetrieveAPIew(generics.RetrieveAPIView):
 #   queryset = Post.all()
  #  serializer_class=PostSerializer

#для изменение
#class PostUpdateAPVIew(generics.UpdateAPIView):
#    queryset = Post.objects.all()
 #   serializer_class = PostSerializer

#для удвление
#class PostDeleteAPIVew(generics.DestroyAPIView):
 #   queryset = Post.objects.all()
  #  serializer_class = PostSerializer

#@api_view(['POST'])#метод запроса от сайта
#def create_post(request):
#   post = request.data
#   serializer = PostSerializer(data=post) #тут мы стереализуем json документ прилетевший из сайта
#    if serializer.is_valid(raise_exception= True):#-этот метод которая пройдется и проверитт заполнил ли правильно
#    serializer.save()
#    return Response(status=201)#у201 - успешно создано


#@api_view(['GET']) #тут декоратор для получение информацию и работа призапросе
#def get_posts(request):
#    posts = Post.objects.all()
#    serualizer = PostSerializer(posts, many=True) #many=True 
#   return Response(serualizer.data) #это команда для ответа


#@api_view(['GET'])
#def get_post(request, pk):
#    post = get_object_or_404(Post, id=pk)
#    serualizer = PostSerializer(post)
#    return Response(serualizer.data)


#@api_view(['PATCH'])
#def patch(request, pk): #поменяяем пост
#    post = get_object_or_404(Post, id =pk)
#    serializer = PostSerializer(instance = post,data = request.data, partial =True)
#     if serializer.is_valid(raise_exception=True):
#        serializer.save()
#       return Response(status=201)



#@api_view(['PUT'])
#def put(request, pk):#функция для изменения
#    post = get_object_or_404(Post, id = pk)
#    serializer = PostSerializer(instance = post, data = request.data)
#    if serializer.is_valid(raise_exception=True):
#       serializer.save()
#       return Response(status = 201)
    
    
#@api_view(['DELETE'])    
#def delete_post(request, pk):
 #   post = get_object_or_404(Post, id=pk)
  #  post.delete()
   # return Response(status=204)



# пишем в виде классов наши функции

