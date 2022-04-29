import json
import pytest

from datetime            import datetime
from django.test         import TestCase, Client
from django.urls         import reverse
from rest_framework      import status
from rest_framework.test import APITestCase

from users.models import User
from ads          import views
from ads.models   import Ad, Result


@pytest.mark.django_db()
class Test_view_create:
    """
    김석재
    """

  # fixture 매 test마다 반복됨
    @pytest.fixture
    def set_user(self, client):
        User.objects.create(
            advertiser = "37445221"
        )
        self.data = {
            "advertiser_id" : "37445221",
            "media"         : "naver",
            "start_date"    : "2022-04-30",
            "end_date"      : "2022-05-30",
            "uid"           : "1819",            
        }
    
    #반복되는 post     
    def create_post(self,client,set_user):
        response = client.post(
            reverse(views.post_create_ad),
            data=self.data
        )
        return response
    
    #POST가 아닌 요청(GET사용)
    def test_create_get(self, client, set_user):
        response=client.get(reverse(views.post_create_ad))             
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
        
        assert response.status_code == 400
        assert response.json() == {'MESSAGE': 'INVALID_DATE'}
    
    # end_day가 start_day보다 전 
    def test_create_ad_with_invalid_end_date(self, client, set_user):
        self.data['start_date'] = "2000-01-15"
        self.data['end_date'] = "2000-01-05"
        response=self.create_post(client, set_user)
       
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


class AdUpdateTest(TestCase):
    """
    권상현
    """
    def setUp(self):
        User.objects.create(advertiser = '37443800')

        Ad.objects.create(
            advertiser_id = '37443800',
            uid = 'ad_12804373131',
            start_date = '2022-05-01',
            end_date = '2022-06-30',
            budget = 10000000,
            estimated_spend = 125000,
            is_delete = False
        )

        Ad.objects.create(
            advertiser_id = '37443800',
            uid = 'ad_12897266083',
            start_date = '2022-07-01',
            end_date = '2022-09-30',
            budget = 20000000,
            estimated_spend = 250000,
            is_delete = True
        )

    def tearDown(self) -> None:
        User.objects.all().delete()
        Ad.objects.all().delete()

    def test_update_success(self):
        """
        광고 세부사항 업데이트 성공
        """
        client = Client()

        data = {
            'budget' : 20000000,
            'estimate_spend' : 250000
        }

        response = client.patch(
            '/advertise/37443800/ad_12804373131', json.dumps(data), content_type = 'application/json'
        )

        self.assertEquals(response.json(),{'MESSAGE': 'SUCCESS'})
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_update_failure_already_delete_ad(self):
        """
        이미 삭제처리 한 광고의 세부사항 업데이트를 시도해 에러 반환
        """
        client = Client()

        data = {
            'budget' : 20000000,
            'estimate_spend' : 250000
        }

        response = client.patch(
            '/advertise/37443800/ad_12897266083', json.dumps(data), content_type = 'application/json'
        )

        self.assertEquals(response.json(),{'MESSAGE':'AD_DOES_NOT_EXIST'})
        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_failure_does_not_exist_ad(self):
        """
        존재하지 않는 광고의 세부사항 업데이트를 시도해 에러 반환
        광고의 세부사항을 업데이트 하기 위해 해당 광고의 디테일 페이지에 들어간다면 uri에 해당 광고의 uid가 적혀 있고
        해당 uri의 정보를 패스파라미터로 읽어 수정할 것이므로 실제로는 존재하지 않을 상황일 가능성이 큼
        """
        client = Client()

        data = {
            'budget' : 20000000,
            'estimate_spend' : 250000
        }

        response = client.patch(
            '/advertise/37443800/ad_1234567890', json.dumps(data), content_type = 'application/json'
        )

        self.assertEquals(response.json(),{'MESSAGE':'AD_DOES_NOT_EXIST'})
        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

"""
    정미정
"""
class AdDeleteTest(APITestCase):
    def setUp(self):
        a = User.objects.create(advertiser="1234")

        self.data = {
            "advertiser_id": "1234",
            "start_date": "2022-04-30",
            "end_date": "2022-05-30",
            "budget": "11.1",
            "estimated_spend": "51.1",
            "uid": "ad-1819",
        }
        self.delete = {
            'is_delete': True,
            'delete_at': datetime.now(),
        }

    def test_delete_advertise(self):
        """
            광고 soft-delete
        """
        b = Ad.objects.create(**self.data)

        response = self.client.delete(
            reverse(views.update_delete_ad,
                    kwargs={
                        'advertiser': b.advertiser,
                        'uid': "ad-1819",
                    }),
            data=self.delete, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_impossible_delete_advertise(self):
        """
            광고의 uid가 일치하지 않을 때 soft-delete 불가
        """
        b = Ad.objects.create(**self.data)

        response = self.client.delete(
            reverse(views.update_delete_ad,
                    kwargs={
                        'advertiser': b.advertiser,
                        'uid': "ad-1810",  # 생성한 uid와 동일하지 않음
                    }),
            data=self.delete, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND) 