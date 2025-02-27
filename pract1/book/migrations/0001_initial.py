# Generated by Django 4.2.19 on 2025-02-27 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('author', models.CharField(max_length=50, verbose_name='author')),
                ('publisher', models.CharField(max_length=50, verbose_name='publisher')),
                ('price', models.IntegerField(verbose_name='price')),
            ],
            options={
                'db_table': 'books',
            },
        ),
    ]
