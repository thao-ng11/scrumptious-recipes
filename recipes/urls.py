from django.urls import path

# from recipes.views import (
#     create_recipe,
#     change_recipe,
#     show_recipe,
#     show_recipes,
# )

# urlpatterns = [
#     path("", show_recipes, name="recipes_list"),
#     path("<int:pk>/", show_recipe, name="recipe_detail"),
#     path("new/", create_recipe, name="recipe_new"),
#     path("edit/", change_recipe, name="recipe_edit"),
# ]

from recipes.views import (
    RecipeCreateView,
    RecipeDeleteView,
    RecipeUpdateView,
    RecipeListtView,
)

urlpatterns = [
    path("", RecipeListtView.as_view(), name="recipe_list"),
    path("<int:pk>/", RecipeDeleteView.as_view(), name="recipe_detail"),
    path("new/", RecipeCreateView.as_view(), name="recipe_new"),
    path("edit/", RecipeUpdateView.as_view(), name="recipe_edit"),
]
