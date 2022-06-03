from django.urls import path

from tags.views import show_tags, show_tag

urlpatterns = [
    path("", show_tags, name="tags_list"),
    path("<int:primary_key>", show_tag, name="tag_detail"),
]
