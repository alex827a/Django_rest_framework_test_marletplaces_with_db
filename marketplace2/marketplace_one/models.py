from django.db import models

# Создание модели категории
class Category(models.Model):
    name = models.CharField(max_length=255)  # Название категории

    class Meta:
        ordering = ('name',)  # Упорядочивание категорий по названию
        verbose_name_plural = 'Categories'  # Во множественном числе будет "Categories"

    def __str__(self):
        return self.name

# Модель продукта
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)  # Добавление связи к категории

    def __str__(self):
        return self.name

# Модель обзора
class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.rating} - {self.product.name}"

""" class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.rating} - {self.product.name}" """