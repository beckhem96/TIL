from django.urls import path
from . import views

app_name = 'articles'


urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    # /articles/1/ => 1번글
    # /articles/2/ => 2번글
    path('<int:pk>/', views.detail, name='detail'),
]
