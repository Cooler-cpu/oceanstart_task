from rest_framework.generics import (
    DestroyAPIView, CreateAPIView
)
from rest_framework import status
from rest_framework.response import Response


from .models import Category
from .serializers import CategorySerializer


class CategoryDestroyView(DestroyAPIView):
    """
    Категория

    Удалить категорию
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        product_count = instance.category_product.all().count()
        if product_count == 0:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            data={'message': "Данная категория используется и не может быть удалена"}, 
            status=status.HTTP_226_IM_USED
        )


class CategoryCreateView(CreateAPIView):
    """
    Категория

    Создать категорию
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
