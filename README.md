# Team_D wanted_project_001_madup

***

## 구성인원 (이름 클릭 시 해당 인원 개인 Github 페이지로 이동)
팀장 [김석재](https://github.com/Cloudblack) <br>
팀원 [권상현](https://github.com/gshduet), [류성훈](https://github.com/rsh1994), [정미정](https://github.com/nxxxtyetdecided)

## 개발기간
2022/04/27 09:00 ~ 2022/04/29 24:00

## 과제 설명
### 과제 주체
[MADUP](https://madup.com/)

### 과제설명
주어진 데이터 셋을 요구사항 대로 서빙하기 위한 관계형 데이터베이스 테이블을 설계하고, 주어진 기능을 제공하는 REST API 서버를 개발하세요.

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
2. 광고주의 정보는 제공 되지 않습니다. 광고주의 정보를 담을 수 있는 테이블을 추가로 만들고 그 광고주와 제공되는 데이터 셋을 연결해서 광고주 CRUD를 할 수 있도록 만들어 주세요.
3. 광고주의 Unique id와 기간으로 검색해 해당 광고주의 매체별 *CTR, ROAS, CPC, CVR, CPA 를 리턴하세요.

***

## 사용된 기술스택
* Backend : Python(3.10.2), Django(4.0.4), Django-rest-framework(3.13.1), MySQL(8.0.28)
* Deploy : Docker
* ETC : Git, Github

## 모델링
![](https://mature-citron-a04.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F3fb98deb-f9df-4fce-a094-a3a2819786f4%2FUntitled.png?table=block&id=340130fa-5309-447e-92ee-b20618903022&spaceId=feb49915-4e9a-4bf7-a86d-f8b150afa4ae&width=2000&userId=&cache=v2)

## 유닛테스트

![](https://velog.velcdn.com/images/gshduet/post/601b9f45-c49b-473a-b83b-6b53cbb76e9b/image.png)

![](https://velog.velcdn.com/images/gshduet/post/220c7257-8de0-4cbf-8327-43c20969340c/image.png)

![](https://velog.velcdn.com/images/gshduet/post/62d75525-e41f-48c7-a283-3ca12413fd4e/image.png)

Django TestCase 라이브러리로 구현된 5개의 유닛테스트와 PyTest로 구현 된 17개의 유닛테스트 

총 22개의 유닛테스트 구현, 통과 완료

## [API 명세서](https://documenter.getpostman.com/view/18212355/UyrGADmN)

## 구현기능 정리
### 김석재
* 광고 생성 API
    - POST 메소드로를 받았을때 동작합니다
    - 필수 항목 (start_date, end_date, advertiser_id, media, uid)이 모두 있어야 생성 할 수 있고 하나라도 없을 시 400 code를 return 합니다.
    - 선택 항목 (budget ,estimated_spend)은 생성에 지장을 주지 않지만 음수 일경우 400 code를 return 합니다
    - Ad를 광고 캠페인이라 가정, Result를 캠페인 기간 매일의 기록이라고 가정해 Ad 기간 만큼 Result를 생성했습니다 (최소 1일)
    - 시작일이 현재 시간보다 이전이거나 종료일이 시작일보다 이전이면 400 code를 return 합니다
- 광고 생성 API 테스트코드 작성
    - 필수 값이 모두 주어졌을 때,선택값이 추가되었을 때 생성 할 수 있음을 테스트합니다
    - 필수 값이 하나라도 없다면 생성 할 수 없음을 테스트합니다
    - start_day가 현재 시간보다 이전일 때, end_day가 start_day보다 이전일 때 생성 할 수 없음을 테스트합니다
    - budget 이 음수일 때, estimated_spend 가 음수일 때 생성 할 수 없음을 테스트합니다
    - 메소드가 POST가 아닌 요청(GET사용) 응답 하지 않음을 테스트합니다

* 광고 생성 API 테스트코드 작성

* Testcase 정립
    - API 동작의 가이드를 만드는 방향으로 구현했습니다

### 권상현
* 프로젝트 초기세팅

* DB 모델링 및 구축, 데이터 입력
    * 자주 조회될 것으로 예상되는 Ad 테이블의 uid, Result 테이블의 uid, media, date 컬럼에 인덱스를 추가했습니다.
    * 제공 받은 로우데이터는 python 

* 광고 상세정보 수정 API
    * 특정 광고의 상세페이지 조회 상황을 패스파라미터로 구현했다 가정하고(*/advertiser_id/uid), 
    * url에서 광고주의 광고 정보를 특정하고 해당 광고의 시작 및 종료시점, 예산, 일 소요예산 등의 변경이 가능하게 하였습니다.
    * 광고의 삭제는 soft_delete 형식으로 구현되어 is_delete 플래그를 통해 삭제 여부를 판단합니다. 이에 따라 해당 광고가 존재하지 않음 상태가 됐음에도 해당 광고를 조회해 변경하는 url을 입력할 경우 DoesNotExist 에러와 함께 404 상태코드를 반환하도록 하였습니다.

* 광고 상세정보 수정 API 테스트코드 작성

### 류성훈
* 광고 결과 조회 API
    * request.GET.get을 사용하여 검색에 필요한 정보인 광고주id(advertiser), 날짜범위(start_date, end_date)를 받도록 하였습니다.
    * object.filter 기능으로 특정 광고주들의 광고데이터들을 필터링 후 결과조회에 필요한 데이터들을 추출했습니다.
    * aggregate로 필요한 필드의 합을 구한 후 필요한 값을 연산한 뒤 math.trunc로 소숫점 셋째자리부터 버림을 하였고. 결과데이터를 반환에 성공할 시 200코드를 return 해줍니다.

* 광고 결과 조회 API 테스트코드 작성

* 로우데이터 분석
    * API를 만들기 전 대략적인 데이터 구조를 확인하고자 pandas를 이용하여 진행하였습니다.
    * csv파일을 읽어들이고, 광고주의 총 수, 미디어 종류와 갯수, 날짜의 최대/최소 등을 확인하였습니다.

### 정미정
* 광고 제거 API
    * soft delete 방식으로 삭제여부 필드가 변경되도록 구현하였습니다.
    * 해당하는 uid가 없을 경우 404코드를 반환합니다.

* 광고 제거 API 테스트코드 작성

* Dockerize
    * Django, My SQL 등 다중 컨테이너 사용을 위해 docker-compose로 구현하였습니다.