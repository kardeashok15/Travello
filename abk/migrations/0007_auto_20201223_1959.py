# Generated by Django 3.1.3 on 2020-12-23 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abk', '0006_memories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memories',
            name='offer',
        ),
        migrations.RemoveField(
            model_name='memories',
            name='price',
        ),
    ]
