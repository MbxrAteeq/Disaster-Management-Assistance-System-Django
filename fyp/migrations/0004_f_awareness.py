# Generated by Django 3.1.4 on 2021-02-26 04:25

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fyp', '0003_e_awareness'),
    ]

    operations = [
        migrations.CreateModel(
            name='F_Awareness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', ckeditor.fields.RichTextField(null=True)),
            ],
        ),
    ]