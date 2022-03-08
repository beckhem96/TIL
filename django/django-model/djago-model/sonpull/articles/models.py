from turtle import update
from django.db import models

# Create your models here.

# models.Model을 상속 받아서 만든다.
class Article(models.Model):
    # Class 속성 : 데이터베이스의 필드 상황
    # CharField
    # CharField.max_length (required) 공식문서 꼭 일어봐라
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
# 변수의 이름을 짓는 패턴
# CamelCase => Class
# snake_case => function, variable