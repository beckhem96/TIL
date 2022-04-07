# Django Model

## 복습

### 가상환경 

```bash
$ python -m venv venv # 가상환경 생성
$ source venv/Scripts/activate # 활성화
```

### .gitignore

한번 실행하고 다음에 더 할 때 편하게 하려고 설정

```
venv/
__pycache__/ # 교수님은 이정도 넣어준다.
```

### django 실행

```bash
$ pip install django==3.2.12 # 사용버전 설치
$ django-admin starproject pjt . # 프로젝트 생성
$ python manage.py startapp articles # 앱 생성
```

- 앱 생성 뒤에 앱을 `settings.py`애 등록한다

- 앱 등록 뒤에 `url`을 분리한다.
- `include`사용하려면 `from django .urls import include` 

- `urlrs.py에 ``path('주소/', include('앱 이름.urls'))`. `name='이름'`은 왠만하면 앱이름으로 통일

### 요청 처리 흐름 

`views.py`에서 

```django
def 이름(request): # request는 필수로 적어줘야함
	return render(request, '폴더이름/파일이름.html')
```

#### base.html

- base.html 쓰는 이유 - 유지보수를 편하게하려고

`settings.py`에 `[BASE_DIR / template]`등록

```django
# base.html

{% block body %} # body든 content든 상관없음
{% endblock body %}

# 이름.html
{% extends 'base.html' %}

{% block body %} # body든 content든 상관없음
	<h1>안녕하세요</h1>
{% endblock body %}
```



name쓰는이유

include 랑 views.이름이랑 뭐가 다름?

```django
{% url 'articles:index' %} # 쓰는 이유 - 나중에 url 바꿔도 파일 내에서 바꾸지 않으려고
```

## MODEL

## Django Model

### Database 기본구조

- 스키마
- 테이블
  - 행
  - 열
- 데이터 베이스트 체계화된 구조

### PK(기본키)

> Modeldms 웹 애플리케이션을 조작하기 위한 개념

### ORM

ORM을 통해서 SQL이 아닌 Django로 DB 조작이 가능

BUT 완전 복합한 서비스는 SQL의 쿼리를 더 복잡하게 짜야하기 때문에 실제로는 같이 활용하는 경우가 있다.

### models.py 작성 (클래스 생성)

Django가 왠만한 건 다 짜놔서 나는 속성?만 조작하면됨` title = models.CharField

```django
from django.db import models

# Create your models here.

# models.Model을 상속 받아서 만든다.
class Article(models.Model):
    # Class 속성 : 데이터베이스의 필드 상황
    # CharField
    # CharField.max_length (required) 공식문서 꼭 일어봐라
    title = models.CharField(max_length=30)
	# TextField
    content = models.TextField()
    
# 변수의 이름을 짓는 패턴
# CamelCase => Class
# snake_case => function, variable
```

### migration

```bash
$ python manage.py makemigrations # mygration 파일 생성
# Select an option: -> 새로 지정할지, 추가할지?
# DB는 무결성이 핵심, 아무튼 1 enter 두번 누르면 된다.
# 교수님 코멘트
# 새로운 필드가 추가되었는데 기본 값이 없다.
# 왜 문제된다? DB에 값이 필수로 ㅣ설정되어 있어서. 빈 값은 존재할 수 없도록 되어 있어서.

# 옵션
# 1. 내가 지금 직접 디폴트 값을 줄게 =>
# 2. 미안. 나 종료하고 models.py에서 내가 직접 설정할게

# 디폴트 값을 파이썬 문법으로 유효한 것을 입력해.
# 너 이거 DateTime인데...2022-03-08 13:17 직접 X 파이썬 코드로 할 수 있도록 도와줌
# 엔타만 누르면 지금 너 timezone
$ python manage.py migrate # DB에 반영

$ python manage.py showmigrations
admin
 [X] 0001_initial
 [X] 0002_logentry_remove_auto_add
 [X] 0003_logentry_add_action_flag_choices
articles
 [X] 0001_initial
auth
 [X] 0001_initial
 [X] 0002_alter_permission_name_max_length
 [X] 0003_alter_user_email_max_length
 [X] 0004_alter_user_username_opts
 [X] 0005_alter_user_last_login_null
 [X] 0006_require_contenttypes_0002
 [X] 0007_alter_validators_add_error_messages
 [X] 0008_alter_user_username_max_length
 [X] 0009_alter_user_last_name_max_length
 [X] 0010_alter_group_name_max_length
 [X] 0011_update_proxy_permissions
 [X] 0012_alter_user_first_name_max_length
contenttypes
 [X] 0001_initial
 [X] 0002_remove_content_type_name
sessions
 [X] 0001_initial
```

## Database API

### DB API

api는 간단하게 조작하는거로 이해(인터페이스)

- Manger
- QuerySet

`Article.objects.all()` - `classname.manager.QuerySet`

### Django Shell

## CRUD

#### CREATE

```python
$ pip install ipython django-extensions # django shell 설치
$ python manage.py shell_plus # 실행

In [1]: Article.objects.all()
Out[1]: <QuerySet []>

In [8]: article = Article() # 클래스 생성, article은 변수, Article()은 클래스 
# Article 뿌리는 models.py애서 옴

# 내용 삽입 1번 객체 조작 + save
In [9]: article.title = '제목' # 값 삽입

In [10]: article.content = '내용입니다.'

In [11]: Article.objects.all() # 아직 반영 안됨
Out[11]: <QuerySet []>

In [12]: article.save() # 저장

In [13]: article # 반영됨
Out[13]: <Article: Article object (1)>

In [14]: Article.objects.all()
Out[14]: <QuerySet [<Article: Article object (1)>]> 

## 내용 삽입 2. 
In [15]: a2 = Article(title='2번글', content='2번내용')

In [16]: a2.save()

In [17]: Article.objects.all()
Out[17]: <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>]>

## 내용 삽입 3. create 메서드

a3 = Article.objects.create(title='제목', content='내용')
```

#### Read

##### all()

> 해당 클래스(테이블) 데이터 조회 => QuerySet

```python
# 1. 전체 데이터 조회
Article.obects.all()
# <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>, <Article: Article object (3)>]>

```

##### get

> 단일 데이터를 조회 => 객체

- 일반적으로 고유한 값(unique)인 경우 사용하는 메서드

  - 결과가 없는 데이터 일 떄 에러 발생

  - 결과가 여러 개 있는 경우 에러 발생

- pk: primary key는 데이터 베이스에서 유맇한 값이므로 pk를 기준으로 조회할 때 사용

```bash
# 2.단일 데이터 조회
Article.objects.get(pk=3)
# <Article: Article object (3)>

# 2-1. 없는 데이터 => 에러
Article.objects.get(pk=100) # 없는 pk는 에러뜸
# DoesNotExist: Article matching query does not exist.

# 2-2. 여러개 있는 경우 => 에러
Article.objects.get(title='제목')
# MultipleObjectsReturned: get() returned more than one Article -- it returned 2!
```

##### filter()

> 여러 데이터를 조회 => QuerySet

````python
# 있는 데이터 조회
Article.objects.filter(title='제목')
# <QuerySet [<Article: Article object (1)>, <Article: Article object (3)>]>

# 없는 데이터 조회
Article.objects.filter(title='헤헤')
# <QuerySet []>

Article.objects.filter(title='제목')[0].content
#  '내용입니다.'

Article.objects.filter(title='제목')[0].id
# 1

Article.objects.filter(title='제목')[0].created_at
#  datetime.datetime(2022, 3, 8, 4, 59, 1, 705799, tzinfo=<UTC>)
````

#### Update

```python
a2 = Article.objects.get(pk=2)
a2.title = '변경된 제목'
a2.save()
```

#### Delete

delete()

```python
a3 = Article.objects.get(pk=3)
a3.delete()
```

### field lookups

조회시 특정 검색 조건을 지정

django 페이지에서 찾아서 사용

### form을 이용한 DB실습

지금 만든 구조가 new form에서 값을 넣으면->view create에서 값을 받아서 데이터베이스에 던져주고->create.html에서 받은걸 보여주고->index에서는 데이터베이스 반복도니까 게시글이 계속 추가되는건가요? 네



번외질문인데 이렇게 삭제되면 데이터는 아예 삭제되는건가요? 아예 삭제됨



그러면 이런거 추적, 복원은 어떻게하나요 db에서 사라지면 복원 안됨

#  Django Form Class

사용자가 입력한 데이터는 개발자가 요구한 형식이 아닐 수 있음을 항상 생각해야함

사용자 입력 데이터를 검증하는 것을 '유효성 검증'이라하는데 코드로 구현하기 힘듦

**Django Form**으로 작업을 줄여줌

- 데이터 손상과 외부 공격에 중요한 방어수단

1. 렌더링을 위한 데이터 준비 및 재구성
2. 데이터에 대한 HTML forms생성
3. 클라이언트로부터 받은 데이터 수신 및 처리

## form 선언

```py
# articles/form.py

from django import forms

class ArticlsForm(forms.Form):
	title = forms.CharField(max_length=10)
	content = fomrs.CharField()
```

## Form rendering options

- <label> & <input> 쌍에 대한 3가지 출력옵션



> Django의 HTML input 요소 표현 방법 2가지

1. form fields
   - input  
2. Widgets
   - 웹페이지 HTML input 요소 렌더링
   - GET?POST 딕셔너리에서 데이터 추출
   - widgets은 반드시 Form fields에 할당됨