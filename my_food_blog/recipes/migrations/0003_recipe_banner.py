# Generated by Django 4.2.18 on 2025-01-30 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_recipe_ingredients'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='banner',
            field=models.ImageField(blank=True, default='fallback.png', upload_to=''),
        ),
    ]
