from django.shortcuts import render
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
    context = {
        'title' : title,
        'content' : content,
    }
    return render(request, 'articles/create.html', context)

def detail(request, pk):
    # 1번 글
    
    article = Article.objects.get(pk=pk)
    
    # 템플릿에서 활용 => context
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)