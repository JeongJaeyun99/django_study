# Generated by Django 4.2.19 on 2025-02-27 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('email', models.CharField(max_length=100, verbose_name='email')),
                ('age', models.IntegerField(verbose_name='age')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
