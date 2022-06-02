from django.db import models


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=20)
    recipes = models.ManyToManyField("recipes.Recipe", related_name="tags")
    food_items = models.ManyToManyField(
        "recipes.FoodItem", null=True, blank=True
    )

    def __str__(self):
        return self.name
