from django.core.management.base import BaseCommand, CommandError
from quickstart.models import ShoeType, ShoeColor

class Command(BaseCommand):
    help = 'Does something with shoes'

    color_choice = [
        "Red",
        "Orange",
        "Yellow",
        "Green",
        "Blue",
        "Indigo",
        "Violet",
        "Black",
        "White",
]
    shoe_choice = [
        'sneaker',
        'boot',
        'sandal',
        'dress',
        'other',
    ]
    def handle(self, *args, **options):
        for color in self.color_choice:
            ShoeColor.objects.create(shoe_color=color)
        for shoe in self.shoe_choice:    
            ShoeType.objects.create(style=shoe)