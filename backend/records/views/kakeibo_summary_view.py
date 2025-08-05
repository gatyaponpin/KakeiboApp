from datetime import datetime
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from records.models import Kakeibo, Subscription
from records.serializers.kakeibo_summary_serializer import KakeiboSummarySerializer

class KakeiboSummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        now = datetime.now()
        current_year = now.year
        current_month = now.month

        income = Kakeibo.objects.filter(
            user=user,
            day__year=current_year,
            day__month=current_month,
            type=Kakeibo.INCOME,
            deleted_at__isnull=True
        ).aggregate(total=Sum('amount'))['total'] or 0

        expense = Kakeibo.objects.filter(
            user=user,
            day__year=current_year,
            day__month=current_month,
            type=Kakeibo.EXPENSE,
            deleted_at__isnull=True
        ).aggregate(total=Sum('amount'))['total'] or 0

        subscription_income = Subscription.objects.filter(
            user=user,
            type=Kakeibo.INCOME
        ).aggregate(total=Sum('amount'))['total'] or 0

        subscription_expense = Subscription.objects.filter(
            user=user,
            type=Kakeibo.EXPENSE
        ).aggregate(total=Sum('amount'))['total'] or 0

        data = {
            "income": income + subscription_income,
            "expense": expense + subscription_expense,
            "balance": income + subscription_income - expense - subscription_expense,
        }

        serializer = KakeiboSummarySerializer(data=data)
        serializer.is_valid(raise_exception=True) 
        return Response(serializer.data)