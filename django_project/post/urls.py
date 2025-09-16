from django.urls import path, include
from rest_framework.routers import DefaultRouter

#from .views import create_post, get_posts, get_post, patch, put,delete_post
#from .views import CreatePostAPIView,PostRetrieveAPIew,PostSerializer,PostDeleteAPIVew,PostListApiiew,PostUpdateAPVIew

#from.views import ListCreatePostAPIiew,RetrievUpdateDestrovPostAPView

#from .views import PostViewSet
from .views import PostModelViewSet

router = DefaultRouter()
#router.register('post', PostViewSet)
router.register('post',PostModelViewSet)

#url-оторый имеет несколькот метод по одной пути Ролтер - это возможность в юсета на определенный метод запроса работает определенный метод
#ролтер более гипкий 

#urlpatterns=[
    #path('get_or_create/',ListCreatePostAPIiew.as_view()),
    #path('post/<int:pk>/',RetrievUpdateDestrovPostAPView.as_view())
#]


urlpatterns = [
    path('',include(router.urls))
    #тут для отдельных классов писали


    #path('create/',CreatePostAPIView.as_view()),
    #path('update/<int:pk>/',PostUpdateAPVIew.as_view()),
    #path('list/',PostListApiiew.as_view()),
    #path('get_post/<int:pk>/',PostRetrieveAPIew.as_view()),
    #path('delete/<int:pk>/',PostDeleteAPIVew.as_view())


    #тут для функции писали 

    
    #path('create/',create_post),
    #path('posts/', get_posts),
    #path('post/<int:pk>/', get_post),
    #path('partial_update/<int:pk>/', patch),
    #path('update/<int:pk>/', put),
    #path('delete/<int:pk>/', delete_post)

]