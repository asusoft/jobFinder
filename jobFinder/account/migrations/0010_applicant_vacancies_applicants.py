# Generated by Django 4.0.1 on 2022-02-21 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_alter_vacancies_updated'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('current_job_sts', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='vacancies',
            name='applicants',
            field=models.ManyToManyField(related_name='job_post', to='account.Applicant'),
        ),
    ]
