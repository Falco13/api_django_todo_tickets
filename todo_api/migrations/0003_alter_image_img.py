# Generated by Django 4.1.6 on 2023-02-14 19:09

from django.db import migrations, models
import todo_api.models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_api', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(upload_to=todo_api.models.image_directory_path),
        ),
    ]
