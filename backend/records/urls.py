from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    UserViewSet,
    CategoryViewSet,
    KakeiboViewSet,
    BudgetViewSet,
    SubscriptionViewSet
)
from .views.budget_summary_view import BudgetSummaryAPIView
from records.views.kakeibo_summary_view import KakeiboSummaryView
from records.views.kakeibo_list_view import KakeiboListView
from .views.token_view import CustomTokenObtainPairView
from .views.regist_user_view import UserRegisterView

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('categories', CategoryViewSet)
router.register('kakeibos', KakeiboViewSet)
router.register('budgets', BudgetViewSet)
router.register('subscriptions', SubscriptionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('budget-summary/', BudgetSummaryAPIView.as_view(), name='budget-summary'),
    path('kakeibo-summary/', KakeiboSummaryView.as_view(), name='kakeibo-summary'),
    path('kakeibo-list/', KakeiboListView.as_view(), name='kakeibo-list'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegisterView.as_view(), name='register'),
]