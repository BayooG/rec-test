from django.core.management.base import BaseCommand, CommandError
from planetly_app.models import UsageType

data_usage = [
    [100, 'electricity', 'kwh', 1.5],
    [101, 'water', 'l', 26.93],
    [102, 'heating', 'kwh', 3.892],
    [103, 'heating', 'l', 8.57],
    [104, 'heating', 'm3', 19.456],
]

class Command(BaseCommand):
    help = 'seeds the usage types values'
    
    
    def handle(self, *args, **options):
        for entry in data_usage:
            data = UsageType(
                id = entry[0],
                name = entry[1],
                unit = entry[2],
                factor = entry[3],
            )
            data.save()