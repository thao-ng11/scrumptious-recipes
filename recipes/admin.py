from logging import StringTemplateStyle
from django.contrib import admin
from recipes.models import Recipe, Step, Ingredient, Measure, FoodItem

# Register your models here.

# Create a class that inherit from admin.ModelAdmin


class RecipeAdmin(admin.ModelAdmin):
    pass


class StepAdmin(admin.ModelAdmin):
    pass


class IngredientAdmin(admin.ModelAdmin):
    pass


class MeasureAdmin(admin.ModelAdmin):
    pass


class FoodItemAdmin(admin.ModelAdmin):
    pass


# Register the class and  model
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Step, StepAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Measure, MeasureAdmin)
admin.site.register(FoodItem, FoodItemAdmin)
