from django.urls import path

from . import views

urlpatterns = [
    path('blogApp/', views.blogFunction, name='blogApp'),
    path('entries/', views.entries, name='entries'),
]