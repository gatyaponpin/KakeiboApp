from rest_framework import serializers
from records.models import Kakeibo

class KakeiboSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kakeibo
        fields = '__all__'