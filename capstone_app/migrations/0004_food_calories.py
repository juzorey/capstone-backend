# Generated by Django 4.2 on 2023-04-17 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("capstone_app", "0003_alter_user_options_alter_user_managers_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="food",
            name="calories",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]