from django.contrib import admin
from .models import Recipe, RecipeIngredients
# from django.contrib.auth import get_user_model

# Register your models here.

class RecipeIngredientInline(admin.StackedInline):
    model = RecipeIngredients
    extra = 0


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    list_display = ["name", "user"]
    raw_id_fields = ["user"]
    readonly_fields = ["timestamp", "updated"]



admin.site.register(Recipe, RecipeAdmin)