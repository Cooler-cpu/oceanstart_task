from adminsortable2.admin import SortableAdminMixin

from django.contrib import admin

from .models import Category


@admin.register(Category)
class CategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass
