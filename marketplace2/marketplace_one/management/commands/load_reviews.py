import json
from django.core.management.base import BaseCommand
from marketplace_one.models import Product, Review

class Command(BaseCommand):
    help = 'Load reviews from a JSON file into the database'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the JSON file with reviews')

    def handle(self, *args, **options):
        with open(options['json_file'], 'r', encoding='utf-8') as file:
            data = json.load(file)
            for entry in data:
                product_id = entry.get('id')  # use  'id' for get product 'id'
                if not product_id:
                    self.stdout.write(self.style.ERROR('Product ID is missing in the JSON entry'))
                    continue
                
                try:
                    product = Product.objects.get(id=product_id)
                except Product.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f'Product not found with ID: {product_id}'))
                    continue

                for review in entry['reviews'][:20]:  # 20 rewiews for one Products
                    Review.objects.create(
                        product=product,
                        rating=review['rating'],
                        comment=review['comment']
                    )
                self.stdout.write(self.style.SUCCESS(f'Successfully loaded reviews for {product.name}'))
