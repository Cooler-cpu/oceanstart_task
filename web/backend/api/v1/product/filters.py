import django_filters
from django_filters.rest_framework import FilterSet

from .models import Product 


class ProductFilter(FilterSet):
    name = django_filters.CharFilter(field_name='name')
    category_id = django_filters.NumberFilter(field_name='category__id')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    is_deleted = django_filters.BooleanFilter(field_name='is_deleted')
    is_published = django_filters.BooleanFilter(field_name='is_published')

    class Meta:
        model = Product
        fields = '__all__'
    