from dataclasses import fields
from django import forms
from .models import Article
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content'] # 직접 지정도 가능
        # fields = '__all__'
        # include, exclude 추천!