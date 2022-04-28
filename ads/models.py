from django.db import models

from core.models import TimeStampModel
   

class Ad(TimeStampModel):
    user = models.ForeignKey('users.User', db_index=True, on_delete=models.CASCADE)  # 광고주 id    
    #uid = models.AutoField( db_index=True, primary_key=True)  # 해당 광고 고유 번호 , 자동 증가추가
    uid = models.CharField(max_length=50, db_index=True, primary_key=True)  # 해당 광고 고유 번호
    start_date = models.DateField(null=True, blank=True)  # 광고 시작 날짜
    end_date = models.DateField(null=True, blank=True)  # 광고 종료 날짜
    budget = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True) # 광고 집행 예산
    estimated_spend = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True) # 일일 광고 집행 예산
    delete_at = models.DateTimeField(null=True, blank=True)  # soft_delete 구현을 위한 컬럼
    is_delete = models.BooleanField(default=False)  # soft_delete 구현을 위한 컬럼

    class Meta :
        db_table = 'ads'


class Result(TimeStampModel):
    ad = models.ForeignKey('Ad', on_delete=models.CASCADE, db_index=True)
    media = models.CharField(max_length=15, db_index=True)
    date = models.DateField(db_index=True)
    cost = models.PositiveIntegerField(default=0)
    impression = models.PositiveIntegerField(default=0)
    click = models.PositiveIntegerField(default=0)
    conversion = models.PositiveIntegerField(default=0)
    cv = models.PositiveIntegerField(default=0)

    class Meta :
        db_table = 'results'
