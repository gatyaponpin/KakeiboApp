from django.core.management.base import BaseCommand
from records.models import Budget, User, Category

class Command(BaseCommand):
    help = '予算データの初期投入'

    def handle(self, *args, **kwargs):
        user = User.objects.get(email='test@test.com')
        category1 = Category.objects.get(category='光熱費/携帯', user=user)
        category2 = Category.objects.get(category='食費', user=user)
        category3 = Category.objects.get(category='交際費', user=user)
        category4 = Category.objects.get(category='雑費', user=user)
        category5 = Category.objects.get(category='固定費', user=user)

        Budget.objects.get_or_create(user=user, category=category1, amount=10000)
        Budget.objects.get_or_create(user=user, category=category2, amount=25000)
        Budget.objects.get_or_create(user=user, category=category3, amount=20000)
        Budget.objects.get_or_create(user=user, category=category4, amount=10000)
        Budget.objects.get_or_create(user=user, category=category5, amount=100000)

        self.stdout.write(self.style.SUCCESS('予算データを投入しました'))
