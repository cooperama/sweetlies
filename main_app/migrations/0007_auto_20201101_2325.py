# Generated by Django 3.1.2 on 2020-11-01 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20201101_1645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='buyers',
        ),
        migrations.DeleteModel(
            name='Buyer',
        ),
    ]
