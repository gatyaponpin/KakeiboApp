from django.core.management.base import BaseCommand
from records.models import Category, User

class Command(BaseCommand):
    help = 'カテゴリーデータの初期投入'

    def handle(self, *args, **kwargs):
        user = User.objects.get(email='test@test.com')

        Category.objects.get_or_create(user=user, category='光熱費/携帯')
        Category.objects.get_or_create(user=user, category='食費')
        Category.objects.get_or_create(user=user, category='交際費')
        Category.objects.get_or_create(user=user, category='雑費')
        Category.objects.get_or_create(user=user, category='固定費')
        
        self.stdout.write(self.style.SUCCESS('カテゴリーデータを投入しました'))