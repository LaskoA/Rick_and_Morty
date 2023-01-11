from django.urls import path
from .views import get_random_character, CharactersListView

app_name = "characters"

urlpatterns = [
    path("characters/random", get_random_character, name="random-character"),
    path("characters/", CharactersListView.as_view(), name="character-list")
]
