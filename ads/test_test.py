from django.test import TestCase
from django.test import Client
import pytest
from ads.models import Ad, Result
from ads.serializers import AdSerializer, ResultSerializer
from django.urls import reverse
from ads import views
<<<<<<< HEAD
from users.models import User
=======

>>>>>>> 58a9947 (error sloved)
# pytestmark = pytest.mark.django_db

# @pytest.mark.django_db(transaction=True)
# class TestUsers:
#     pytestmark = pytest.mark.django_db
#     def test_my_user(self):
#         me = Ad.objects.last()
#         print(me)
#         assert me.is_superuser


<<<<<<< HEAD
# .view test
# create

@pytest.mark.django_db()
class Test_view_create:
    """
    김석재
    """

  # fixture 매 test마다 반복됨
    @pytest.fixture
    def set_user(self, client):
        User.objects.create(
            advertiser="37445221"
        )
        self.data = {
            "advertiser_id": "37445221",
            "media": "naver",
            "start_date": "2022-04-30",
            "end_date": "2022-05-30",
            "uid": "1819",            
        }
    
    #반복되는 post     
    def create_post(self,client,set_user):
        response = client.post(
            reverse(views.get_create_ad),
            data=self.data
        )
        return response
    
    #POST가 아닌 요청(GET사용)
    def test_create_get(self, client, set_user):
        response=client.get(reverse(views.get_create_ad))             
        assert response.status_code == 405
        assert response.json() == {'detail': 'Method "GET" not allowed.'}
        

    # 필수 값
    def test_create_ad(self, client, set_user):        
        response=self.create_post(client, set_user)        
        assert response.status_code == 200
        assert Ad.objects.count() == 1
        assert Result.objects.count() == 31
    
    # 필수 값 + 선택 값
    def test_create_ad_with_more_value(self, client, set_user):
        self.data['estimated_spend'] = "11.1"
        self.data['budget'] = "11.5"
        response=self.create_post(client, set_user) 
        assert response.status_code == 200
        assert Ad.objects.count() == 1
        assert Result.objects.count() == 31

    # 필수 값이 누락
    def test_create_ad_without_start_date(self, client, set_user):
        self.data['start_date'] = ""
        response=self.create_post(client, set_user)
        assert response.status_code == 400
        assert response.json() == {'MESSAGE': 'MISSING_VALUE'}

    def test_create_ad_without_end_date(self, client, set_user):
        self.data['end_date'] = ""
        response=self.create_post(client, set_user)
        assert response.status_code == 400
        assert response.json() == {'MESSAGE': 'MISSING_VALUE'}

    def test_create_ad_without_advertiser_id(self, client, set_user):
        self.data['advertiser_id'] = ""
        response=self.create_post(client, set_user)
        assert response.status_code == 400
        assert response.json() == {'MESSAGE': 'MISSING_VALUE'}

    def test_create_ad_without_media(self, client, set_user):
        self.data['media'] = ""
        response=self.create_post(client, set_user)
        assert response.status_code == 400
        assert response.json() == {'MESSAGE': 'MISSING_VALUE'}

    def test_create_ad_without_uid(self, client, set_user):
        self.data['uid'] = ""
        response=self.create_post(client, set_user)
        assert response.status_code == 400
        assert response.json() == {'MESSAGE': 'MISSING_VALUE'}
    
    # start_day가 오늘보다 전   
    def test_create_ad_with_invalid_start_date(self, client, set_user):
        self.data['start_date'] = "1500-01-15"
        response=self.create_post(client, set_user)
        print(response.status_code,response.json())
        assert response.status_code == 400
        assert response.json() == {'MESSAGE': 'INVALID_DATE'}
    
    # end_day가 start_day보다 전 
    def test_create_ad_with_invalid_end_date(self, client, set_user):
        self.data['start_date'] = "2000-01-15"
        self.data['end_date'] = "2000-01-05"
        response=self.create_post(client, set_user)
        print(response.status_code,response.json())
        assert response.status_code == 400
        assert response.json() == {'MESSAGE': 'INVALID_DATE'}
        
    #budget 이 음수
    def test_create_ad_with_negative_budget(self, client, set_user):
        self.data['budget'] = "-1"
        response=self.create_post(client, set_user)
        assert response.status_code == 400
        assert response.json() == {'MESSAGE': 'INVALID_VALUE'}
    
    #estimated_spend 가 음수
    def test_create_ad_with_negative_estimated_spend(self, client, set_user):
        self.data['estimated_spend'] = "-1"
        response=self.create_post(client, set_user)
        assert response.status_code == 400
        assert response.json() == {'MESSAGE': 'INVALID_VALUE'}
        
    

# 필수 항목 없이 광고 생성 post ()


=======
@pytest.mark.django_db()
class Testview:
    def test_url(self, client):
        response = client.get(reverse(views.ad_list))
        assert response.status_code == 200

    def test_db(self, client):
        response = client.post(
            reverse(views.get_create_ad),
            data={
                "user_id": "37",
                "media": "naver",
                "start_date": "2022-04-30",
                "end_date": "2022-05-30",
                "uid": "1819",
                "budget": "11.1",
                "estimated_spend": "51.1"
            }
        )

        assert False


# .view test

# create
# 광고 생성 post (필수항목 media, start date, end date)


# 필수 항목 없이 광고 생성 post ()
>>>>>>> 58a9947 (error sloved)
def test_create_ad_without_required():
    pass
# 선택 항목을 추가하여 광고 생성 post (선택항목을 추가하여 광고 생성)


def test_create_ad_with_more_value():
    pass


# read

<<<<<<< HEAD

def test_create_ad_with_required(client):
    pass
=======
@pytest.mark.django_db()
def test_create_ad_with_required(client):
    response = client.get(reverse(views.ad_list))
    assert response.status_code == 200
>>>>>>> 58a9947 (error sloved)
# 광고 조회 get(광고주 id)


def test_index_with_advertiser_id():
    pass
# 존재하지 않는 id로 광고 조회 get(없는 광고주 id)


def test_index_with_null_advertiser_id():
    pass
# 주어지는 값 없이 광고 조회 get()


def test_index_without_value():
    pass
# 광고 조회 get(광고주 id , 기간)


def test_index_with_advertiser_id_and_period():
    pass
# 광고주 id 없이 광고 조회 get(기간)


def test_index_without_advertiser_id():
    pass


# update

# 광고 부분 수정 patch (광고주 id, 광고 id)
# 무엇을 수정할 수 있는지 아직 정해지지않음
def test_update_ad_with_advertiser_id_and_ad_id():
    pass
# 광고주 id로 수정 patch(광고주 id)


def test_update_ad_with_advertiser_id():
    pass
# 광고 id로 수정 patch(광고 id)


def test_update_ad_with_ad_id():
    pass
# 값 없이 수정 patch()


def test_update_ad_without_value():
    pass

# delete

# 광고 소프트 삭제 delete (광고주 id, 광고 id )


def test_soft_delete_ad_with_advertiser_id_and_ad_id():
    pass
# 광고주 id로만 소프트 삭제 delete (광고주 id)


def test_soft_delete_ad_with_advertiser_id():
    pass
# 광고 id로만 소프트 삭제 delete (광고 id )


def test_soft_delete_ad_with_ad_id():
    pass
# 값 없이 소프트 삭제 delete ()


def test_soft_delete_ad_without_value():
    pass
# 소프트 삭제후 DB에 남아있는지 체크


def test_soft_delete_ad_check_db():
    pass
