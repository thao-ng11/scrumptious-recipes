from logging import StringTemplateStyle
from django.contrib import admin
from recipes.models import Recipe, Step, Ingredient

# Register your models here.

# Create a class that inherit from admin.ModelAdmin


class RecipeAdmin(admin.ModelAdmin):
    pass


class StepAdmin(admin.ModelAdmin):
    pass


class IngredientAdmin(admin.ModelAdmin):
    pass


# Register the class and  model
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Step, StepAdmin)
admin.site.register(Ingredient, IngredientAdmin)
