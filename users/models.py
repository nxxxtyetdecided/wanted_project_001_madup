from django.db import models

from core.models import TimeStampModel


class User(TimeStampModel) :
    advertiser = models.CharField(max_length=15, primary_key=True)  # 광고주 고유 번호

    class Meta :
        db_table = 'users'

