from datetime import datetime
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from records.models import Category, Budget, Kakeibo, Subscription
from records.serializers.budget_summary_serializer import BudgetSummarySerializer

class BudgetSummaryAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        now = datetime.now()
        current_year = now.year
        current_month = now.month
        categories = Category.objects.filter(user=user)

        data = []
        for category in categories:
            budget = Budget.objects.filter(user=user, category=category).first()

            income = Kakeibo.objects.filter(
                user=user,
                category=category,
                day__year=current_year,
                day__month=current_month,
                type=Kakeibo.INCOME
            ).aggregate(total=Sum('amount'))['total'] or 0

            expense = Kakeibo.objects.filter(
                user=user,
                category=category,
                day__year=current_year,
                day__month=current_month,
                type=Kakeibo.EXPENSE
            ).aggregate(total=Sum('amount'))['total'] or 0

            subscription = Subscription.objects.filter(
                user=user,
                category=category
            ).aggregate(total=Sum('amount'))['total'] or 0


            data.append({
                "category_name": category.category,
                "amount": budget.amount if budget else None,
                "total": subscription + expense - income,
            })

        serializer = BudgetSummarySerializer(data, many=True)
        return Response(serializer.data)