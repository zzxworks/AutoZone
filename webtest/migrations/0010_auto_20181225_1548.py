# Generated by Django 2.1.1 on 2018-12-25 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webtest', '0009_auto_20181225_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webcasestep',
            name='webcomments',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='备注'),
        ),
    ]
