# Generated by Django 4.1 on 2022-09-12 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0003_alter_selection_items"),
    ]

    operations = [
        migrations.AlterField(
            model_name="selection",
            name="items",
            field=models.ManyToManyField(blank=True, null=True, to="ads.ad"),
        ),
    ]
