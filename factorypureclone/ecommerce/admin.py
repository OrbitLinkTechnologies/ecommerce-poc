from django.contrib import admin
from .models import ProductReview, ProductQuestion, Generator

# Register your models here.
admin.site.register(ProductReview)
admin.site.register(ProductQuestion)
admin.site.register(Generator)