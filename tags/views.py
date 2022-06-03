from django.shortcuts import redirect, render

try:
    from tags.models import Tag
except Exception:
    Tag = None


# Create your views here.


def show_tags(
    request,
):
    context = {
        "tags": Tag.objects.all() if Tag else None,
    }
    return render(request, "tags/list.html", context)


def show_tag(request, primary_key):
    tag = Tag.objects.get(pk=primary_key)
    print(tag)

    return render(request, "tags/detail.html")
