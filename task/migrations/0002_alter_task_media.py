# Generated by Django 4.0.1 on 2022-02-11 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='media',
            field=models.FileField(blank=True, default=5, upload_to='task/%Y/%m/%d/', verbose_name='Тапшырма'),
            preserve_default=False,
        ),
    ]
