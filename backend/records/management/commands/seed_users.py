from django.core.management.base import BaseCommand
from records.models import User

class Command(BaseCommand):
    help = 'ユーザー初期データの投入'

    def handle(self, *args, **kwargs):
        User.objects.get_or_create(
            email='admin@example.com',
            password='admin',
            username='管理者',
        )
        User.objects.get_or_create(
            email='test@test.com',
            password='test',
            username='test',
        )
        self.stdout.write(self.style.SUCCESS('ユーザーを投入しました'))
