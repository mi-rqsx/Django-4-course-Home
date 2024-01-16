# Generated by Django 4.2.7 on 2024-01-16 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_alter_categories_options_alter_categories_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL'),
        ),
        migrations.AddField(
            model_name='products',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.CharField(default='', max_length=150, unique=True, verbose_name='Название'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(default='', max_length=150, unique=True, verbose_name='Название'),
            preserve_default=False,
        ),
    ]