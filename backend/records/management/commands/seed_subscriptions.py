from django.core.management.base import BaseCommand
from records.models import Subscription, User, Category

class Command(BaseCommand):
    help = 'サブスクリプションデータの初期投入'

    def handle(self, *args, **kwargs):
        user = User.objects.get(email='test@test.com')
        category = Category.objects.get(user=user, category='固定費')

        Subscription.objects.get_or_create(user=user, category=category, name='家賃', amount=71770, day=1)
        Subscription.objects.get_or_create(user=user, category=category, name='奨学金', amount=10530, day=1)
        Subscription.objects.get_or_create(user=user, category=category, name='ジム', amount=3300, day=1)
        Subscription.objects.get_or_create(user=user, category=category, name='保険', amount=10000, day=1)
        Subscription.objects.get_or_create(user=user, category=category, name='Apple Music', amount=1000, day=1)
        Subscription.objects.get_or_create(user=user, category=category, name='Amazon Prime', amount=600, day=1)
        self.stdout.write(self.style.SUCCESS('サブスクリプションデータを投入しました'))