# Generated by Django 4.2 on 2023-05-06 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Like', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='main_category',
            name='icons',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
