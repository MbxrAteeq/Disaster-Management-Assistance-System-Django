# Generated by Django 3.1.4 on 2021-02-26 03:52

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fyp', '0002_auto_20210215_1931'),
    ]

    operations = [
        migrations.CreateModel(
            name='E_Awareness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', ckeditor.fields.RichTextField(null=True)),
            ],
        ),
    ]
