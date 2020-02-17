from django.core.management.base import BaseCommand
from suggestions.models import Suggestion
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = "This command deletes expired suggestions"

    def handle(self, *args, **options):
        Suggestion.objects.filter(
            created__lte=datetime.now() - timedelta(days=2)
        ).delete()
        self.stdout.write("Deleted suggestions older than 2 days")
