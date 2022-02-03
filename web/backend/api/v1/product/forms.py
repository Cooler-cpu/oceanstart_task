from django import forms
from django.core.exceptions import ValidationError

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def clean_categories(self):
        categories = self.cleaned_data.get('categories')
        categories_count = categories.count()
        if categories_count < 2 or categories_count > 10:
            raise ValidationError("У товара может быть от 2х до 10 категорий")

        return categories