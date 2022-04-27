from django.test import TestCase
from django.test import Client

#.view test
class question_view_tests(TestCase):
    #def setUp(self) :        
    #def tearDown(self):
        
    #create    
    # 광고 생성 post (필수항목 media, start date, end date)
    def test_create_ad_with_required(self):
        self.assertEqual(1 + 1, 3)
    # 필수 항목 없이 광고 생성 post () 
    def test_create_ad_without_required(self):
        pass   
    # 선택 항목을 추가하여 광고 생성 post (선택항목을 추가하여 광고 생성)
    def test_create_ad_with_more_value(self):
        pass   
    
    
    #read        
    # 광고 조회 get(광고주 id)
    def test_index_with_advertiser_id(self):
        pass
    # 존재하지 않는 id로 광고 조회 get(없는 광고주 id) 
    def test_index_with_null_advertiser_id(self):
        pass
    # 주어지는 값 없이 광고 조회 get()
    def test_index_without_value(self):
        pass
    # 광고 조회 get(광고주 id , 기간)
    def test_index_with_advertiser_id_and_period(self):
        pass
    # 광고주 id 없이 광고 조회 get(기간)
    def test_index_without_advertiser_id(self):
        pass
    
    
    #update
    
    # 광고 부분 수정 patch (광고주 id, 광고 id)
    # 무엇을 수정할 수 있는지 아직 정해지지않음
    def test_update_ad_with_advertiser_id_and_ad_id(self):
        pass
    # 광고주 id로 수정 patch(광고주 id)
    def test_update_ad_with_advertiser_id(self):
        pass
    # 광고 id로 수정 patch(광고 id)
    def test_update_ad_with_ad_id(self):
        pass
    # 값 없이 수정 patch()
    def test_update_ad_without_value(self):
        pass
    
    #delete
    
    # 광고 소프트 삭제 delete (광고주 id, 광고 id )
    def test_soft_delete_ad_with_advertiser_id_and_ad_id(self):
        pass
    # 광고주 id로만 소프트 삭제 delete (광고주 id)
    def test_soft_delete_ad_with_advertiser_id(self):
        pass
    # 광고 id로만 소프트 삭제 delete (광고 id )
    def test_soft_delete_ad_with_ad_id(self):
        pass
    # 값 없이 소프트 삭제 delete ()
    def test_soft_delete_ad_without_value(self):
        pass
    # 소프트 삭제후 DB에 남아있는지 체크 
    def test_soft_delete_ad_check_db(self):
        pass