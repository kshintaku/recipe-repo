from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:recipe_id>/", views.recipeView, name="detail"),
    path("search/<str:search_term>", views.searchView, name="search"),
    path("<str:category>/", views.index, name="category"),
]
