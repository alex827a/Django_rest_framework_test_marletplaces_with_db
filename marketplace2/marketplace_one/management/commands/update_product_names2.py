from django.core.management.base import BaseCommand
from marketplace_one.models import Product
import os

class Command(BaseCommand):
    help = 'Update product names from a text file, disregarding exact count matching'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the text file containing product names')

    def handle(self, *args, **options):
        file_path = options['file_path']
        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR('File does not exist'))
            return

        with open(file_path, 'r', encoding='utf-8') as file:
            # Получаем список названий, очищаем от пробелов и разбиваем по разделителю
            new_names = [name.strip() for name in file.read().split(';') if name.strip()]

        # Получаем список товаров из базы данных
        items = list(Product.objects.all().order_by('id'))

        # Обновляем названия товаров в пределах доступных имен
        for item, new_name in zip(items, new_names):
            item.name = new_name
            item.save()
            self.stdout.write(self.style.SUCCESS(f'Updated product {item.id} name to {new_name}'))

        self.stdout.write(self.style.SUCCESS(f'Updated names for the first {min(len(items), len(new_names))} products'))
