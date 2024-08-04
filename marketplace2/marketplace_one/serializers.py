from rest_framework import serializers
from .models import Product, Review, Category

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'rating', 'comment']

class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)  # Отзывы, уже добавленные в вашем сериализаторе
    category_name = serializers.CharField(source='category.name', read_only=True)  # Добавление поля имени категории

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category_name', 'reviews']  # Включение 'category_name' и 'reviews'
