# Generated by Django 4.0.4 on 2022-10-21 02:54

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='previous_work',
            field=ckeditor.fields.RichTextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='profile',
            name='skills',
            field=ckeditor.fields.RichTextField(max_length=2000),
        ),
    ]
