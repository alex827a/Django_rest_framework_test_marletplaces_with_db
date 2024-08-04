from django.core.management.base import BaseCommand
from marketplace_one.models import Product, Category
import random
import decimal

class Command(BaseCommand):
    help = 'Generate random products in the database'

    def add_arguments(self, parser):
        parser.add_argument('num_products', type=int, help='Number of products to create')
        parser.add_argument('category_name', type=str, help='Category name for the products')

    def handle(self, *args, **options):
        num_products = options['num_products']
        category_name = options['category_name']

        # Finding category if cant find create new category 
        category, created = Category.objects.get_or_create(name=category_name)
        if created:
            self.stdout.write(self.style.SUCCESS(f'Category "{category_name}" created.'))

        for i in range(num_products):
            name = f'Product {i + 1}'
            description = f'Description for Product {i + 1}'
            price = decimal.Decimal(random.randrange(100, 10000)) / 100
            Product.objects.create(name=name, description=description, price=price, category=category)
        
        self.stdout.write(self.style.SUCCESS(f'Successfully created {num_products} products in category "{category_name}".'))
