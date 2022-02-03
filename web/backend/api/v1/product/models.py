from django.db import models

from api.v1.category.models import Category


class Product(models.Model):
    name = models.CharField("Название продукта", max_length=100)
    categories = models.ManyToManyField(
        Category, verbose_name="Категории", related_name="category_product"
    )
    price = models.FloatField("Цена")
    is_deleted = models.BooleanField("Удаленный товар")
    is_published = models.BooleanField("Товар опубликован", default=True)
    ordering = models.PositiveIntegerField('Сортировка', default=0, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['ordering']
