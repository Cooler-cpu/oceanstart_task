from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import SearchFilter
from rest_framework import status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import Product
from .serializers import ProductSerializer
from .filters import ProductFilter


class ProductListCreateView(ListCreateAPIView):
    """
    Продукт

    Создать, получить список продуктов
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ('$categories__name',)
    filter_class = ProductFilter


class ProductRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    Продукт

    Просмотр, редактирование и удаление продукта
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return Response(status=status.HTTP_202_ACCEPTED)


