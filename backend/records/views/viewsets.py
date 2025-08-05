from rest_framework import viewsets
from records.models import User, Category, Kakeibo, Budget, Subscription
from records.serializers import (
    UserSerializer,
    CategorySerializer,
    KakeiboSerializer,
    BudgetSerializer,
    SubscriptionSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class KakeiboViewSet(viewsets.ModelViewSet):
    queryset = Kakeibo.objects.all()
    serializer_class = KakeiboSerializer


class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer