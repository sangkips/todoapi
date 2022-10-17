from django.urls import path, include
from rest_framework import routers
from .views import TodoViewSet, UserViewSet, GroupViewSet


router = routers.DefaultRouter()
router.register(r'todo', TodoViewSet)
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)


urlpatterns = [
    path('', include(router.urls)),
   
]