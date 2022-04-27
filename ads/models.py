from django.db import models
from django.forms import SelectDateWidget

from core.models import TimeStampModel


class Ad(TimeStampModel):
    user = models.ForeignKey('users.User', db_index=True, on_delete=models.CASCADE)  # 광고주 id
    uid = models.CharField(max_length=50, primary_key=True)  # 해당 광고 고유 번호
    start_date = models.DateField(null=True, blank=True)  # 광고 시작 날짜
    end_date = models.DateField(null=True, blank=True)  # 광고 종료 날짜
    budget = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True) # 광고 집행 예산
    estimated_spend = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True) # 일일 광고 집행 예산
    delete_at = models.DateTimeField(null=True, blank=True)  # soft_delete 구현을 위한 컬럼
    is_delete = models.BooleanField(default=False)  # soft_delete 구현을 위한 컬럼

    class Meta :
        db_table = 'ads'


class Result(TimeStampModel):
    ad = models.ForeignKey('Ad', on_delete=models.CASCADE)
    media = models.CharField(max_length=15)
    date = models.DateField()
    cost = models.PositiveIntegerField()
    impression = models.PositiveIntegerField()
    click = models.PositiveIntegerField()
    conversion = models.PositiveIntegerField()
    cv = models.PositiveIntegerField()

    class Meta :
        db_table = 'results'
