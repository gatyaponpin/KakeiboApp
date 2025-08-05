from rest_framework import serializers

class KakeiboSummarySerializer(serializers.Serializer):
    income = serializers.IntegerField()
    expense = serializers.IntegerField()
    balance = serializers.IntegerField()