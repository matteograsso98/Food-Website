from django.db import models

class Recipe(models.Model):
    recipename = models.CharField(max_length=255)
    ingredients = models.CharField(max_length=255, null=True)
    media = models.ImageField(upload_to= 'recipes/images/', null=True)
     
    def __str__(self):
        return f"{self.recipename}" 
    #def __str__(self):
        #return self.name
