from django.db import models
from .user import User

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="ユーザー")
    category = models.CharField(max_length=100, verbose_name="カテゴリー名")
    balance = models.BooleanField(default=False, verbose_name="収支区分")
    created_at = models.DateField(auto_now_add=True, verbose_name="作成日")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日")
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name="削除日")

    def __str__(self):
        return self.category