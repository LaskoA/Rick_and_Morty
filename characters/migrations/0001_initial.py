# Generated by Django 4.1.5 on 2023-01-11 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_id', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=255)),
                ('species', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Genderless', 'Genderless'), ('Unknown', 'Unknown')], max_length=20)),
                ('image', models.URLField(max_length=255, unique=True)),
            ],
        ),
    ]