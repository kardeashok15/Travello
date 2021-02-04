# Generated by Django 3.1.3 on 2020-12-21 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abk', '0004_auto_20201213_1900'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('price', models.IntegerField()),
                ('desc', models.TextField()),
                ('offer', models.BooleanField()),
            ],
        ),
    ]
