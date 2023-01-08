from django.db import transaction
from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType
from ecommerce.models import BaseProduct

# we were reading this SO thread: https://django-polymorphic.readthedocs.io/en/latest/migrating.html
# but we couldn't figure it out so we just deleted all models and started fresh

class Command(BaseCommand):
  help = "Migrating our data models to be polymorphic"

  @transaction.atomic
  def handle(self, *args, **kwargs):
    self.stdout.write("Updating Model to be Polymorphic...")
    # Create all the game console
    new_ct = ContentType.objects.get_for_model(BaseProduct)
    BaseProduct.objects.filter(polymorphic_ctype__isnull=True).update(polymorphic_ctype=new_ct)