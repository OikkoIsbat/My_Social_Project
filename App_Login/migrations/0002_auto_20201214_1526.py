# Generated by Django 3.1.4 on 2020-12-14 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='full_name',
            field=models.CharField(blank=True, max_length=264),
        ),
    ]
