# Generated by Django 4.2 on 2023-08-04 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Like', '0006_item_guaranteed_time_item_color_name_item_model_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='about_your_business',
            field=models.TextField(blank=True, null=True),
        ),
    ]