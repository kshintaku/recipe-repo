from django.contrib import admin

# Register your models here.
from .models import Recipe


class RecipeAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            "Recipe information",
            {"fields": ["name", "image", "recipe", "img_url", "category"]},
        ),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    list_display = ("name", "pub_date")


admin.site.register(Recipe, RecipeAdmin)
