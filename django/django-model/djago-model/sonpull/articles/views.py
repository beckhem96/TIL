from django.shortcuts import redirect, render
from .models import Article

# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    article = Article()
    article.title = title 
    article.content = content 
    article.save()
    context = {
        'title' : title,
        'content' : content,
    }
    return redirect('articles:detail', article.pk)

def detail(request, pk):
    # 1번 글
    
    article = Article.objects.get(pk=pk)
    
    # 템플릿에서 활용 => context
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    # 1. 값 가져오기
    title = request.GET.get('title')
    content = request.GET.get('content')
    # 2. DB 수정
    article = Article.objects.get(pk=pk)
    article.title = title 
    article.content = content 
    article.save()
    # 3. redirect 상세 페이지로!
    return redirect('articles:detail', article.pk)