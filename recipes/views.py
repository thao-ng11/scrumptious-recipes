from django.shortcuts import redirect, render

try:
    from recipes.forms import RecipeForm
    from recipes.models import Recipe
except Exception:
    RecipeForm = None
    Recipe = None


class RecipeCreateView(CreateView):
    model = Recipe
    fields = [
        "name",
        "author",
        "description",
        "image",
    ]


template_name = "recipes/create.html"

# def create_recipe(request):
#     if request.method == "POST" and RecipeForm:
#         form = RecipeForm(request.POST)
#         if form.is_valid():
#             recipe = form.save()
#             return redirect("recipe_detail", pk=recipe.pk)
#     elif RecipeForm:
#         form = RecipeForm()
#     else:
#         form = None
#     context = {
#         "form": form,
#     }
#     return render(request, "recipes/new.html", context)
class RecipeDeleteView(DeleteView):
    model = Recipe
    success_url = reverse_lazy("recipes_list")


# If you delete a recipe, they need to know where
# to send the user once it is done


class RecipeUpdateView(UpdateView):
    model = Recipe
    fields = [
        "name",
        "author",
        "description",
        "image",
    ]
    template_name = "recipes/edit.html"


# def change_recipe(request, pk):
#     if Recipe and RecipeForm:
#         instance = Recipe.objects.get(pk=pk)
#         if request.method == "POST":
#             form = RecipeForm(request.POST, instance=instance)
#             if form.is_valid():
#                 form.save()
#                 return redirect("recipe_detail", pk=pk)
#         else:
#             form = RecipeForm(instance=instance)
#     else:
#         form = None
#     context = {
#         "form": form,
#     }
#     return render(request, "recipes/edit.html", context)


class RecipeListtView(ListView):
    model = Recipe
    template_name = "recipes/list.html"


# def show_recipes(request):
#     context = {
#         "recipes": Recipe.objects.all() if Recipe else [],
#     }
#     return render(request, "recipes/list.html", context)


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipes./detail.html"


# def show_recipe(request, pk):
#     context = {
#         "recipe": Recipe.objects.get(pk=pk) if Recipe else None,
#     }
#     return render(request, "recipes/detail.html", context)
