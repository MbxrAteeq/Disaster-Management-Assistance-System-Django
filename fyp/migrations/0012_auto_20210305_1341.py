# Generated by Django 3.1.4 on 2021-03-05 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fyp', '0011_auto_20210305_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.FileField(default='photos/avatar.png', upload_to=''),
        ),
    ]
