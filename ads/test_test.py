from django.test import TestCase
from django.test import Client
import pytest
from ads.models import Ad, Result
from ads.serializers import AdSerializer, ResultSerializer
from django.urls import reverse
from ads import views

# pytestmark = pytest.mark.django_db

# @pytest.mark.django_db(transaction=True)
# class TestUsers:
#     pytestmark = pytest.mark.django_db
#     def test_my_user(self):
#         me = Ad.objects.last()
#         print(me)
#         assert me.is_superuser


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
def test_create_ad_without_required():
    pass
# 선택 항목을 추가하여 광고 생성 post (선택항목을 추가하여 광고 생성)


def test_create_ad_with_more_value():
    pass


# read

@pytest.mark.django_db()
def test_create_ad_with_required(client):
    response = client.get(reverse(views.ad_list))
    assert response.status_code == 200
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
