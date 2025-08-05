from rest_framework import serializers
from records.models import Kakeibo

class KakeiboListSerializer(serializers.ModelSerializer):
    type_label = serializers.SerializerMethodField()
    category_name = serializers.CharField(source='category.category', read_only=True)

    class Meta:
        model = Kakeibo
        fields = [
            'id',
            'name',
            'amount',
            'type',
            'type_label',
            'day',
            'memo',
            'category_id',
            'category_name',
            'created_at'
        ]

    def get_type_label(self, obj):
        return '収入' if obj.type == Kakeibo.INCOME else '支出'