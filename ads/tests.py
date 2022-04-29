import json

from django.test import TestCase, Client
from rest_framework import status

from users.models import User
from ads.models import Ad


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
