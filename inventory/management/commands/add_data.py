import json
from django.core.management.base import BaseCommand

from inventory.models import Items, Products, Categories


class Command(BaseCommand):
    help = 'Adding data in Items, Products and Categories tables.'
  
    def add_arguments(self, parser):
        parser.add_argument('category_config', type=str)
        parser.add_argument('product_config', type=str)
        parser.add_argument('item_config', type=str)

    def handle(self, *args, **options):
        with open(options['category_config']) as f:
            category_config_json = json.load(f)

        for cat in category_config_json:
            category, is_created = Categories.objects.get_or_create(
                name = cat['name'],
                isactive = cat['isactive']
            )

            if not is_created:
                category.save()

        with open(options['product_config']) as g:
            product_config_json = json.load(g)

        for pro in product_config_json:
            product, is_created = Products.objects.get_or_create(
                name = pro['name'],
                category = Categories.objects.get(name = pro['category']),
                isactive = pro['isactive']
            )

            if not is_created:
                product.save()

        with open(options['item_config']) as h:
            item_config_json = json.load(h)

        for ite in item_config_json:
            item, is_created = Items.objects.get_or_create(
                name = ite['name'],
                product = Products.objects.get(name = ite['product']),
                isactive = ite['isactive'],
                quantity = ite['quantity']
            )

            if not is_created:
                item.save()

