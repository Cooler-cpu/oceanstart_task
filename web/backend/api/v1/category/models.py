from django.db import models


class Category(models.Model):
    name = models.CharField("Название категории", max_length=100)
    ordering = models.PositiveIntegerField('Сортировка', default=0, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['ordering']
    