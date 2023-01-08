from django.db import transaction
from django.core.management.base import BaseCommand

from ecommerce.models import GameConsole
from ecommerce.management.commands.factories import (
    GameConsoleFactory
)

game_console = GameConsoleFactory()
game_console.product_name
game_console.product_category
game_console.product_manufacturer
game_console.product_brand
game_console.product_SKU
game_console.product_condition
game_console.product_quantity
game_console.product_photos
game_console.game_console_classification_type

object_count = 5

class Command(BaseCommand):
    help = "Generates Game Console test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [GameConsole]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")
        # Create all the game consoles
        game_consoles = []
        for _ in range(object_count):
            game_console = GameConsoleFactory()
            game_consoles.append(game_console)