from django.contrib import admin
from .models import Recipe

# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
  list_display = ("recipename", "ingredients")

admin.site.register(Recipe, RecipeAdmin)