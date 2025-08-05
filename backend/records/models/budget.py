from django.db import models
from .user import User
from .category import Category

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="ユーザー")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="カテゴリ")
    amount = models.IntegerField(verbose_name="金額")
    memo = models.CharField(max_length=256, null=True, blank=True, verbose_name="メモ")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日")
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name="削除日")

    def __str__(self):
        return f"{self.user.name} - {self.category.name} : {self.amount}円"