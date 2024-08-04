# myapp/management/commands/update_product_names.py
from django.core.management.base import BaseCommand
from marketplace_one.models import Product
import os

class Command(BaseCommand):
    help = 'Update product names from a text file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the text file containing product names')

    def handle(self, *args, **options):
        file_path = options['file_path']
        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR('File does not exist'))
            return

        with open(file_path, 'r') as file:
            content = file.read()
            new_names = [name.strip() for name in content.split(';') if name.strip()]

        # Check if the number of products in database matches the number of names in the file
        if Product.objects.count() != len(new_names):
            self.stdout.write(self.style.ERROR('The number of products does not match the number of names provided'))
            return

        # Update product names
        for item, new_name in zip(Product.objects.all().order_by('id'), new_names):
            item.name = new_name
            item.save()
            self.stdout.write(self.style.SUCCESS(f'Updated product {item.id} name to {new_name}'))

        self.stdout.write(self.style.SUCCESS('All product names updated successfully'))
