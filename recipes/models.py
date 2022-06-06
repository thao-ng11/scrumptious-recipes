from django.db import models

# One


class Recipe(models.Model):
    name = models.CharField(max_length=125)
    author = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField(
        null=True, blank=True
    )  # blank allowed to have image as optional
    created = models.DateTimeField(auto_now_add=True)  # record the timestamp
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + " by " + self.author


# Many
class Step(models.Model):
    recipe = models.ForeignKey(
        "Recipe",
        related_name="steps",
        on_delete=models.CASCADE,
    )
    order = models.PositiveSmallIntegerField()
    directions = models.TextField(max_length=300)

    def __str__(self):
        return f"{self. recipe} Step  {self.order}"


class Measure(models.Model):

    name = models.CharField(max_length=30, unique=True)
    abbreviation = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.abbreviation}"


class FoodItem(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    amount = models.FloatField(validators=[MaxValueValidator(20)])
    recipe = models.ForeignKey(
        "Recipe",
        related_name="ingredients",
        on_delete=models.CASCADE,
    )
    measure = models.ForeignKey(
        "Measure",
        on_delete=models.PROTECT,
    )
    food = models.ForeignKey(
        "FoodItem",
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return f"{self.amount} {self. measure} {self.food}"
