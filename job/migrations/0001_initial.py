# Generated by Django 4.2.1 on 2023-05-21 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.CharField(max_length=100)),
                ('applicant_username', models.CharField(max_length=100)),
            ],
        ),
    ]
