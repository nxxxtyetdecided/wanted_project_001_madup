from ads.models     import Ad, Result
from rest_framework import serializers

class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = "__all__"

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = "__all__"
