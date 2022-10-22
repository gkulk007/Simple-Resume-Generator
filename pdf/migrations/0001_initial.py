# Generated by Django 4.0.4 on 2022-10-21 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('summary', models.TextField(max_length=2000)),
                ('degree', models.CharField(max_length=255)),
                ('school', models.CharField(max_length=255)),
                ('university', models.CharField(max_length=255)),
                ('previous_work', models.TextField(max_length=2000)),
                ('skills', models.TextField(max_length=2000)),
            ],
        ),
    ]
