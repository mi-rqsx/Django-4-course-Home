# Generated by Django 4.2.7 on 2024-01-16 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(blank=True, max_length=200, null=True, unique=True)),
            ],
            options={
                'db_table': 'category',
            },
        ),
    ]