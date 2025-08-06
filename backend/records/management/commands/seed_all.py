from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = "Run all seeders"

    def handle(self, *args, **kwargs):
        seeders = [
            'seed_users',
            'seed_categories',
            'seed_subscriptions',
            'seed_budgets',
            'seed_kakeibos',
        ]
        for cmd in seeders:
            call_command(cmd)
        self.stdout.write(self.style.SUCCESS('All seeders executed.'))