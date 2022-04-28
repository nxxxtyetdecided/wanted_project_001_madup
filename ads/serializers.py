from rest_framework import serializers
from .models import Ad

class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['user','uid','start_date','end_date','budget','estimated_spend','delete_at','is_delete']
