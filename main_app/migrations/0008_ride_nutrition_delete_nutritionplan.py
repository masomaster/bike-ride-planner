# Generated by Django 4.1.2 on 2022-10-27 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_nutritionplan'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='nutrition',
            field=models.ManyToManyField(to='main_app.nutrition'),
        ),
        migrations.DeleteModel(
            name='NutritionPlan',
        ),
    ]