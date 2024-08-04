# your_app/views.py
from rest_framework import viewsets
from .models import Product, Review
from .serializers import ProductSerializer, ReviewSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ReviewViewSet(viewsets.ModelViewSet):
     queryset = Review.objects.all()
     serializer_class = ReviewSerializer
     def get_queryset(self):
        product_id = self.kwargs.get('product_id')
        if product_id:
            return self.queryset.filter(product=product_id)
        return self.queryset
class ProductReviewsViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_id'])