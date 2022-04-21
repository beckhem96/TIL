## Customizing authentication in Django



뭘 까먹었다

https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#substituting-a-custom-user-model

![image-20220413142638218](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20220413142638218.png)

이순서로 해주면 됨

Auth_USER_MODEL에 나의 앱 유저로 바꿔주고

위애 대로 하면

Accounts에 admin 생김

![image-20220413143013019](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20220413143013019.png)

### 회원 가입 오류

![image-20220413143142573](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20220413143142573.png)



### 장고에서 app이 실행되는 순서

#### 1. INSTALLED_APP에서 순차적으로 APP IMPORT

#### 2. 각 앱의 models를 import

### django에서 user 모델을 참조할때

#### 1. models.py에서는` settings.AUTH_USER_MODEL`

#### 2. models.py를 제외한 다른 모든 곳은 get_user_model()