from django.db import models
from .user import User
from .category import Category
from datetime import date

class Kakeibo(models.Model):
    INCOME = 1
    EXPENSE = 2

    TYPE_CHOICES = (
        (INCOME, '収入'),
        (EXPENSE, '支出'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="ユーザー")
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.PROTECT, verbose_name="カテゴリ")
    type = models.SmallIntegerField(choices=TYPE_CHOICES, default=EXPENSE) 
    name = models.CharField(max_length=20, null=True, blank=True, verbose_name="収支名")
    amount = models.IntegerField(verbose_name="金額")
    memo = models.CharField(max_length=256, null=True, blank=True, verbose_name="メモ")
    day = models.DateField(default=date.today, verbose_name="日付")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日")
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name="削除日")

    def __str__(self):
        return f"{self.user.name} - {self.amount}円"