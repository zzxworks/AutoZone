# Generated by Django 2.1.1 on 2018-11-20 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_robotframework', '0002_auto_20181120_1452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='edit_case_step',
            name='webcase',
        ),
    ]
