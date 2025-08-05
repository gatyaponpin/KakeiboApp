from rest_framework import serializers

class BudgetSummarySerializer(serializers.Serializer):
    category_name = serializers.CharField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2, allow_null=True)
    total = serializers.IntegerField()