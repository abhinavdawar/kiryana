from django.contrib import admin

from inventory.models import Categories, Items, Products

# Register your models here.
admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(Items)