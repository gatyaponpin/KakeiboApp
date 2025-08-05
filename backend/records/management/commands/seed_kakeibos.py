from django.core.management.base import BaseCommand
from records.models import Kakeibo, User, Category
from datetime import date

class Command(BaseCommand):
    help = '家計簿データの初期投入'

    def handle(self, *args, **kwargs):
        user = User.objects.get(email='test@test.com')
        category1 = Category.objects.get(category='光熱費/携帯', user=user)
        category2 = Category.objects.get(category='食費', user=user)
        category3 = Category.objects.get(category='交際費', user=user)
        category4 = Category.objects.get(category='雑費', user=user)

        Kakeibo.objects.get_or_create(user=user, category=category1, name='電気代', amount=3345, day=date(2025, 8, 1))
        Kakeibo.objects.get_or_create(user=user, category=category1, name='ガス代', amount=4350, day=date(2025, 8, 1))
        Kakeibo.objects.get_or_create(user=user, category=category1, name='携帯', amount=4912, day=date(2025, 8, 1))
        Kakeibo.objects.get_or_create(user=user, category=category2, name='アイコス', amount=530, day=date(2025, 8, 1))
        Kakeibo.objects.get_or_create(user=user, category=category2, name='コンビニ', amount=638, day=date(2025, 8, 1))
        Kakeibo.objects.get_or_create(user=user, category=category2, name='飲み物', amount=152, day=date(2025, 8, 1))
        Kakeibo.objects.get_or_create(user=user, category=category2, name='肉屋', amount=1170, day=date(2025, 8, 2))
        Kakeibo.objects.get_or_create(user=user, category=category2, name='八百屋', amount=255, day=date(2025, 8, 2))
        Kakeibo.objects.get_or_create(user=user, category=category2, name='ヨーク', amount=777, day=date(2025, 8, 3))
        Kakeibo.objects.get_or_create(user=user, category=category2, name='モンスター', amount=230, day=date(2025, 8, 4))
        Kakeibo.objects.get_or_create(user=user, category=category3, name='物販', amount=4300, day=date(2025, 8, 1))
        Kakeibo.objects.get_or_create(user=user, category=category3, name='居酒屋', amount=5000, day=date(2025, 8, 2))
        Kakeibo.objects.get_or_create(user=user, category=category4, name='漂白剤', amount=218, day=date(2025, 8, 2))

        self.stdout.write(self.style.SUCCESS('家計簿データを投入しました'))
