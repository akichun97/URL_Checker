# Generated by Django 4.2 on 2024-06-20 12:40

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0002_remove_url_state_url_states"),
    ]

    operations = [
        migrations.RenameField(
            model_name="url",
            old_name="states",
            new_name="state",
        ),
    ]
