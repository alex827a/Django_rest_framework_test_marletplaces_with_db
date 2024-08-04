import os
import json
import requests
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Fetch data from API endpoints using token authentication'

    def handle(self, *args, **options):
        token = "e6e993473467a4978dff850002dac70f252a9c06"  # Используйте переменные окружения в продакшене для хранения токенов
        if not token:
            self.stdout.write(self.style.ERROR('Token not found. Please set the TOKEN environment variable.'))
            return

        # Пример запроса данных о конкретном продукте (если ID известен и статичен)
        product_url = "http://127.0.0.1:8000/api/products/101/"  # URL для конкретного продукта
        headers = {'Authorization': f'Token {token}'}

        response = requests.get(product_url, headers=headers)
        if response.status_code == 200:
            product_data = response.json()
            # Сохраняем или обрабатываем данные о продукте
            with open('product_data.json', 'w') as f:
                json.dump(product_data, f, indent=4)
            self.stdout.write(self.style.SUCCESS('Successfully fetched and stored product data.'))
        else:
            self.stdout.write(self.style.ERROR(f"Failed to fetch product data. Status: {response.status_code}"))
            self.stdout.write(self.style.ERROR(response.text))
