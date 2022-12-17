from django.contrib import admin
from .models import ProductReview, ProductQuestion, Generator, Customer, Price
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(ProductReview)
admin.site.register(ProductQuestion)
admin.site.register(Generator)

# Define an inline admin descriptor for Customer model
# which acts a bit like a singleton
class CustomerInline(admin.StackedInline):
    model = Customer
    can_delete = False
    verbose_name_plural = 'customer'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [CustomerInline]

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

class PriceInlineAdmin(admin.TabularInline):
  model = Price
  extra = 0

class ProductAdmin(admin.ModelAdmin):
  inlines = [PriceInlineAdmin]

admin.site.unregister(Generator)
admin.site.register(Generator, ProductAdmin)