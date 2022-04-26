# Team_D wanted_project_001_madup

***

## 구성인원 (이름 클릭 시 해당 인원 개인 Github 페이지로 이동)
팀장 [김석재](https://github.com/Cloudblack) <br>
팀원 [권상현](https://github.com/gshduet), [류성훈](https://github.com/rsh1994), [정미정](https://github.com/nxxxtyetdecided)

## 개발기간
2022/04/27 09:00 ~ 2022/04/30 09:00

## 과제 설명
### 과제 주체
[MADUP](https://madup.com/)

### 과제설명
주어진 데이터 셋을 요구사항 대로 서빙하기 위한 관계형 데이터베이스 테이블을 설계하고, 주어진 기능을 제공하는 REST API 서
버를 개발하세요.

### 출제의도
DB의 데이터를 이용해 API를 구현하는 기본적인 설계 및 개발 능력을 보기 위함

### 개발조건
1. Database
  * (필수)
    * 테이블 명 컬럼명은 Snake Case 사용 해 주세요!
    * Index 설정 해주세요!
  * (가산점)
    *데이터 증가에 따라 최대한 일정한 응답 시간을 가질 수 있는 방향으로 디자인 하시면 가산점이 있습니다.
2. Server
  * (필수)
    * REST API 를 지원하는 웹프레임워크를 사용하세요.
    * 테스트 코드를 작성 해 주세요.
    * API 기능만 구현해 주세요.
    * RESTful 의 의미를 잘 생각해서 구현해주세요. (Endpoint URL, HTTP Method)
    * Response는 JSON 형식으로 리턴해야 합니다.
    * SQL Alchemy, Peewee, Django ORM, JPA, Hibernate 등 ORM 을 사용하고, Raw 는 사용할 수 없습니다.
  * (가산점)
    * 요구된 사항만 구현되는 서버가 아니라, 다른 많은 기능이 함께 있는 서버라고 생각하시고, 폴더, 파일, 코드 스트럭처를 짜임새 있게 정리해 주세요.
    * DB Migration Tool (Alembic, Django Migration, flyway 등) 를 사용하면 가산점이 있습니다.
      * Migration History를 Repository에 함께 업로드 해주세요.
    * Dockerize 하면 가산점이 있습니다.

### 요구사항
1. 시작 후 72시간내에 제출 해 주세요.
2. 광고주의 정보는 제공 되지 않습니다. 광고주의 정보를 담을 수 있는 테이블을 추가로 만들고 그 광고주와 제공되는 데이터 셋
을 연결해서 광고주 CRUD를 할 수 있도록 만들어 주세요.
3. 광고주의 Unique id와 기간으로 검색해 해당 광고주의 매체별 *CTR, ROAS, CPC, CVR, CPA 를 리턴하세요.

***

## 사용된 기술스택
* Backend : Python(3.10.2), Django(4.0.4), Django-rest-framework(3.13.1), MySQL(8.0.28)
* Deploy : AWS EC2(예정), AWS RDS(예정), Docker(예정)
* ETC : Git, Github

## 모델링


## API 명세서


## 구현기능 정리
### 권상현

### 김석재

### 류성훈

### 정미정


## 설치 및 구동방법
