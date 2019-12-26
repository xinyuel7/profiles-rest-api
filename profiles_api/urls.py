from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet) #queryset don't need a base_name

urlpatterns = [
    path('Hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls)),
]
