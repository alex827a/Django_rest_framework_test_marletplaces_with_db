import requests
import json
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Fetch and save product data with reviews'

    def handle(self, *args, **options):
        token = 'd8b9d3ef06bd1d3f19c8bb1bf34b11a13c759e19'  # Use environment variables or secure means to store token
        headers = {'Authorization': f'Token {token}'}
        response = requests.get('http://127.0.0.1:8079/api/products/', headers=headers)

        if response.status_code == 200:
            products = response.json()
            with open('products_and_reviews.json', 'w') as f:
                json.dump(products, f, indent=4)
            self.stdout.write(self.style.SUCCESS('Successfully fetched and stored product data with reviews.'))
        else:
            self.stdout.write(self.style.ERROR(f"Failed to fetch products. Status: {response.status_code}"))
            self.stdout.write(self.style.ERROR(response.text))
