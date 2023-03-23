from rest_framework import serializers
from .models import Product, Rating


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "description", "price"]


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ["id", "rating", "description"]
    
    def create(self, validated_data):
        product_id = self.context["product_id"]
        user_id = self.context["user_id"]
        rating = Rating.objects.create(product_id = product_id, user_id=user_id, **self.validated_data)
        return rating