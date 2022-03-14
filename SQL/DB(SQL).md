

# SQL

## DB

- 체계화된 데이터의 모임
- 저료 항목의 중복을 없애고 자료를 구조화하여 기억시켜 놓은 자료의 집합체

### 데이터 베이스로 얻는 장점

- 중복 최소화
- 무결성(정확한 정보를 저장)
- 일관성
- 독립성(물리적/논리적)
- 표준화
- 보안 유지

## RDB

### 관계형 데이터베이스

- 키와 값들의 간단한 관계를 표 형태로 정리한 DB
- 관계형 모델에 기반

### 용어 정리

스키마 : DB에서 자료구조, 관계 등 전반적인 명세를 기술한 것

테이블 : 행과 열의 모델을 사용해 조직된 데이터 요소들의 집합

열 : 고유한 데이터 형삭아 자종

행 : 실제 데이터가 저장되는 형태

기본키 : 각 행의 고유값, 반드시 설정, DB 관리 및 관계 설정 시 주요하게 활용

## SQLite Data Type

1. NULL
2. INTERGER 
3. REAL - 부동 소수점 값
4. TEXT
5. BLOB - 입력된 그대로 정확히 저장된 데이터

## SQL

- 관계형 데이터베이스 관리시스템의 데이터 관리를 위해 설계된 프로그래밍 언어

- 데이터 스키마 조정

- RDBMS를 조작하는 언어

### SQL 분류

- DDL
  - 관계형 구조를 정의하기 위한 명령어
    - CREATE
    - DROP
    - ALTER
- DML
  - 데이터를 저장, 조회, 수정, 삭제 등을 하기 위한 명령어
    - INSERT
    - SELECT
    - UPDATE
    - DELETE
- DCL
  - 사용자의 권한 제어를 위해 사용
    - GRANT
    - REVOKE
    - COMMIT
    - ROLLBACK

```bash
$ sqlite3 tutorial.sqlite3 # tutorial.sqlite3이란 DB생성
> .database   # .은 sqlite 프로그램의 기능을 실행하는 것
> .model csv
> .import hellodb.csv examples
> .tables # csv 파일을 table로 만들기

> SELECT * FROM examples; # ;까지 하나의 명령으로 간주. SELECT문은 특정 테이블의 레코드 정보를 반환
id,first_name,last_name,age,country,phone
1,"길동","홍",600,"충청도",010-0000-0000
> .headers on  # 출력형식 변경됨
> SELECT * FROM examples;
id,first_name,last_name,age,country,phone
1,"길동","홍",600,"충청도",010-0000-0000
> .model column
> SELECT * FROM examples;
id  first_name  last_name  age  country  phone
--  ----------  ---------  ---  -------  -------------
1   길동          홍          600  충청도      010-0000-0000


```

DB우클릭 후 NEW QUERY

### CREATE

```sqlite
-- SQLite new query 작성
CREATE TABLE classmates (
 id INTERGER PRIMARY KEY,
 name TEXT
); --작성 후에 우클릭 run query로 살행
  
INSERT INTO classmates (id, name) VALUES (1, '홍길동'); --run selected query로 특정 쿼리만 실행
```

bash에서도 CREATE 가능

```bash
# 생성
sqlite> CREATE TABLE classmates (
   ...> id INTERGER PRIMARY KEY,
   ...> name TEXT
   ...> );
sqlite> .tables # 확인
classmates  examples
# 조회
sqlite> .schema classmates 
CREATE TABLE classmates (
  id INTERGER PRIMARY KEY,
  name TEXT
  );
```

### DROP

```sql
DROP TABLE classmates; # SQL에서 싷행
```

```bash
# 석재, terminal에서 실행
sqlite> DROP TABLE classmates;
sqlite> .table
examples
```

```bash
CREATE TABLE classmates ( # SQL에서 작성 후 실행
  name TEXT,
  age INT, 
  address TEXT
  );
# 터미널에서 조회
sqlite> .schema classmates
CREATE TABLE classmates (
  name TEXT,
  age INT,
  address TEXT
  );
```

### INSERT

- insert는 특정 테이블에 행(레코드)을 삽입

```sql
INSERT INTO classmates (name, age) VALUES ('임완택', 25); # sql에 작성 후 실행
```

```bash
sqlite> SELECT * FROM classmates # 터미널에서 확인
   ...> ;
name  age  address
----  ---  -------
임완택   25
```

```sql
INSERT INTO classmates VALUES ('임완택', 25, '용인'); # 모든 열에 데이터가 있으면 행 명시안해도 됨
```

```bash
sqlite> SELECT * FROM classmates;
name  age  address
----  ---  -------
임완택   25
임완택   25   용인
```

- id가 없는 이유는 SQLite가 관리해주고 있었기 때문이다.
- SQLite는 따로 PK속정을 작성하지 않으면 자동으로 PK 옵션을 가진 rowid 컬럼을 정의



지금까지 sqlite로 db 테이블 확인하던 걸로 확인 가능



sqlite3 파일 우클릭 후에 뉴쿼리 클릭하고 저장하면 sql 파일이 만들어짐

```sql
--SQLite
SElECT * FROM examples;

INSERT INTO classmates(name, age) VALUES ('이름', 25)

INSERT INTO classmates VALUES ('이름', 25, '서울') # 모든 컬럼을 사용하면 컬럼 명시 안해보 됨

sqlite> SELECT * FROM classmates; # 주소처럼 필요한 정보는 공백으로 비워두면 안됨 -> NOT NULL 설정
name  age  address
----  ---  -------
임완택   25
임완택   25   용인

# NOT NULL 설정
sqlite> CREATE TABLE classmates (
   ...> id INTERGER PRIMARY KEY,
   ...> name TEXT NOT NULL,
   ...> age INT NOT NULL,
   ...> address TEXT NOT NULL
   ...> );
   
sqlite> INSERT INTO classmates VALUES ('홍길동', 30, '서울'); # 스키마에 id를 직접 작성해서 입력 column을 명시하지않으면 자동입력 안됨
Parse error: table classmates has 4 columns but 3 values were supplied

sqlite> INSERT INTO classmates VALUES (1, '임완택', 27, '용인'); 
sqlite> SELECT * FROM classmates; # 데이터 삽입됨
id  name  age  address
--  ----  ---  -------
1   임완택   27   용인

sqlite> INSERT INTO classmates (name, age, address) VALUES ('홍길동', 30, '서울'); # 
sqlite> SELECT * FROM classmates; # 컬럼 명시해주면 오류 X
id  name  age  address
--  ----  ---  -------
1   임완택   27   용인
    홍길동   30   서울
    
INSERT INTO classmates VALUES
('임완택', 27, '용인'),
('임싸피', 30, '인천'),
('임철수', 25, '부산'),
('임동수', 28, '대구'),
('임광철', 31, '춘천');
    
sqlite> SELECT * FROM classmates;
name  age  address
----  ---  -------
임완택   27   용인
임싸피   30   인천
임철수   25   부산
임동수   28   대구
임광철   31   춘천
sqlite> SELECT rowid, * FROM classmates; # rowid로 편하게 id 생성
rowid  name  age  address
-----  ----  ---  -------
1      임완택   27   용인
2      임싸피   30   인천
3      임철수   25   부산
4      임동수   28   대구
5      임광철   31   춘천 

```

### READ

LIMIT

WHERE

DISTINCT

```sql
SELECT 컬럼1, 컬러2, .... FROM TABLE

# LIMIT - 반환되는 행 수를 제한, OFFSET키워드와 함계 사용하면 특정 행부터 LIMIT 걸수 있음
sqlite> SELECT * FROM classmates LIMIT 3 OFFSET 2; # 2번 쨰 다음부터 3개 
name  age  address
----  ---  -------
임철수   25   부산
임동수   28   대구
임광철   31   춘천
# WHERE - 조건 지정
sqlite> SELECT * FROM classmates WHERE age>=30;
name  age  address
----  ---  -------
임싸피   30   인천
임광철   31   춘천
sqlite> SELECT * FROM classmates WHERE address='용인';
name  age  address
----  ---  -------
임완택   27   용인
# DISTINCT - 출력될 떄 중복제거, SELECT 바로 뒤에 작성
```

### DELETE

```sql
# 중복 불가능 값인 id로 조건 지정해서 삭제
DELETE FROM 테이블 WHERE 조건;
```

### AUTOINCREMENT

```sql
CREATE TABLE 테이블 (
id INTERGER PRIMARY KEY AUTOCREMENTl, # Django에서 기본으로 설정
): # SQLite가 사용되자 않은 값이나 삭제된 행의 값 재사용금지
```

### UPDATE

```sql
# 조건을 통해 특정 레코드 수정하기
# 이것도 중복 불가능한 값 id를 기준으로 수정
UPDATE 테이블 SET 컬럼1=값1, .... WHERE 조건;
```

### SQLite Aggregate Functions

```sql
# COUNT - 그룹의 항목 수를 가져옴
SELECT COUNT(컬럼) FROM 테이블;
# AVG - 모든 값의 평균
SELECT AVG(컬럼) FROM 테이블;
# MAX - 그룹에 있는 모든 값의 최댓값
SELECT MAX컬럼) FROM 테이블;
# MIN - 그룹에 있는 모든 값의 최솟값
SELECT MIN(컬럼) FROM 테이블;
# SUM - 모든 값의 합을 계산
SELECT SUM(컬럼) FROM 테이블;
# 위 함수들 모두 컬럼이 INTERGER일 떄 사용 가능 
```

### LIKE

```sql
# 와일드 카드 2가지 패턴
% #이자리에 문자열이 있을수도 없을 수도 있음
_ # 반드시 이자리에 한개의 분자가 존재햐야함
```

### ODER BY

```sql
# 정렬, ASC - 오름차순, DESC - 내림차순
SELECT * FROM 테이블 ODER BY 컬럼 ASC;
SELECT * FROM 테이블 ODER BY 컬럼1, 컬럼2 DESC;
```

### GROUP BY

```sql
# SELECT 문의 optional 절
# 문장에 WHERE이 있으면 WHERE 뒤에 작성
SELECT 컬럼1, aggregate_function(컬럼2) FROM 테이블 GROUP BY 컬럼1, 컬럼2;
# AS 를 사용해서 컬럼명 바꿔서 조회 가능
SELECT 컬럼1 AS 별명 FROM 테이블 GROUP BY 컬럼;
```

### ALTER TABLE

```sql
# 1. 테이블 이름 변경
# 2. 테이블에 새로운 column 추가
# 3. 컬럼 이름 수정 (new in sqlite 3.25.0)
ALTER TABLE 테이블 RENAME COLUMN 현재이름 TO 바꿀 이름
# 컬럼 추가
ALTER TABLE 테이블 ADD COLUMN 컬럼이름 데이터타입 설절;
# 새로운 추가 필드에 대한 정보가 없어서 NOT NULL 형태의 컬럼은 추가 X
# 해결방법 1. NOT NULL 설정없이 컬럼 추가 2. 기본 값(DEFALUT) 설정
ALTER TABLE 테이블 ADD COLUMN 컬럼이름 데이터타입 설절 NOT NULL DEFAUL '기본 값';
```



## SQL & Django







## Q

>  교수님 혹시 데이터베이스 테이블 생성할 때 기본키를 설정안하면 시스템 내에서 알아서 기본키를 지정해주나요?

일반적으로 PK는 직접 지정을 해주시는 것이 좋습니다. DBMS에 따라 명시적으로 설정되지 않는 경우 다른 값들을 대체해서 사용할 수 있긴 합니다

> 교수님 DB api중에 orm을 쓰는 django orm이 있고 오늘 배운 sql도 있는게 맞나요? 연관 관계가 db api > (django orm, sql) 이렇게 이해해도 될까요?

아니요! SQL은 DB를 사용하는 유일한 언어인데 Django ORM은 Object 조작으로 DB 조작이 가능하도록 하는 ORM 종류 중에 하나입니다

DB API 는 그냥 DB를 활용하기 위한 인터페이스들을 뜻해요! python으로도 조작 가능합니다. 

> rowid외 PK지정한 Id 차이점

## TIP

수정떄나 생성 떄 updated_at =

1. template 와 관련된 문제 많음 상속, template language 등 

2. 디테일하게 좀 외워야할 필요가 있음

3. GET과 POST를 썼을 떄 코드의 차이점

4. model 생성 방법들 1, 2, 3

5. admin site

   ```python
   class ArticleAdmin(admin.ModelAdmin):
       list_display = ('id', 'title', 'created_at', 'updated_at')
       
   admin.site.register(Article, ARticleAdmin)
   ```

6. settings.py -> DATABASES 'ENGINE' 봐바

7. 각각 tempalte, 함수, 구조들을 분리한 이유, 어떻게 작동하는지 자세히 공부할 필요가 있음

## QnA

산업, 직무에 관련경험이 없어도 본인이 가지고 있는 SW 역량을 어필하면 될 것 같다.

큰시스템을 다뤄본 적이 없다고 생각하고 코테로 어느 정동 소프트웨어 역량은 검증 가능, 자신이 가지고 있는 역량 어필이 중요하다.

학습역량 어필, 프로젝트 진행 과정 중 겪은 어려움과 해결 방법