# Generated by Django 5.0 on 2023-12-20 10:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="update",
            new_name="updated",
        ),
    ]
