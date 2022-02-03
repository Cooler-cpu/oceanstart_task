from rest_framework import serializers

from .models import Product
from api.v1.category.serializers import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Product
        exclude = ["ordering"]

    def validate_categories(self, value):
        categories_count = len(value)
        if categories_count < 2 or categories_count > 10:
            raise serializers.ValidationError("У товара может быть от 2х до 10 категорий")
        return value
