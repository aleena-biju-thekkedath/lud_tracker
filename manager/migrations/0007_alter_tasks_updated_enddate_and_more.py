# Generated by Django 4.2.4 on 2023-09-11 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("manager", "0006_alter_tasks_updated_enddate_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tasks",
            name="updated_enddate",
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name="tasks",
            name="updated_startdate",
            field=models.DateTimeField(null=True),
        ),
    ]
