# Generated by Django 4.2.4 on 2023-09-01 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("manager", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="proj_desc",
            field=models.CharField(default="NA", max_length=1000),
        ),
    ]
