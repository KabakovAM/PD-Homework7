from django.contrib import admin
from . import models


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk','category_name']
    ordering = ['pk']
    search_fields = ['category_name']
    search_help_text = 'Поиск по названию'
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['category_name'],
            },
        ),
    ]


class RecipeAdmin(admin.ModelAdmin):
    list_display = ['pk', 'recipe_name', 'reg_data', 'author', 'category_name']
    ordering = ['pk']
    list_filter = ['recipe_name', 'reg_data', 'category_name']
    search_fields = ['pk']
    search_help_text = 'Поиск по ID'
    readonly_fields = ['reg_data']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['picture', 'recipe_name', 'description', 'time', 'category_name'],
            },
        ),
        (
            'Рецепт',
            {
                'classes': ['collapse'],
                'fields': ['products','steps'],
            },
        ),
    ]


admin.site.register(models.Recipe, RecipeAdmin)
admin.site.register(models.Category, CategoryAdmin)
