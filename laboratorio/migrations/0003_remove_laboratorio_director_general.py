# Generated by Django 4.1.1 on 2023-08-07 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0002_laboratorio_director_general_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='laboratorio',
            name='director_general',
        ),
    ]