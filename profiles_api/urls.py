from django.urls import path
from profiles_api import views
urlpatterns = [
    path('Hello-view/', views.HelloApiView.as_view())
]
