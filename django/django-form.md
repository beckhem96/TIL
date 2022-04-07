Wyhy model Form

- HTML Form : 사용자로부터 정보를 받아서 서버에 전송하는 양식

- 데이터베이트스에 저장(django Model)
- 스키마 필드(필드 변경)

사용자가 입력받는 거 하드코딩 안하고 바로 db에 저장



**Q** forms.py에서 파이썬식 조건/반복문 사용 가능한가요? 템플릿에서 dtl식 조건/반복문 썼던것처럼..

**A** 가능도 하지만 기본적으로 내부에서 쓸 일은 별로 없을 것이다.



```python
from django import forms
from . models import Article

# ModelForm은 모델의 필드로 HTMl을 만들어줌
# 필요한 정보? 모델/필드
# ArticleForm의 정보를 담는 Meta 클래스

class ArticleForm(forms.ModelForm):
	class Meta:
	model = Article
	fields = '__all__'
    
    
source

# is_valid() modelform에 속한 메소드
```

자연어 강의 추천

https://www.youtube.com/watch?v=jqykPH3jbic&list=PLetSlH8YjIfUpPbSAfsY4zBJfztlH9CSQ

https://www.edwith.org/ai331