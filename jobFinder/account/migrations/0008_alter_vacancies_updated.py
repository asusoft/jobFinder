# Generated by Django 4.0.1 on 2022-02-21 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_vacancies_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancies',
            name='updated',
            field=models.DateTimeField(),
        ),
    ]
