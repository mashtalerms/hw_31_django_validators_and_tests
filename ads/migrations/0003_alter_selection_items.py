# Generated by Django 4.1 on 2022-09-12 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="selection",
            name="items",
            field=models.ManyToManyField(null=True, to="ads.ad"),
        ),
    ]
