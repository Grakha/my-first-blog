# Generated by Django 3.0.4 on 2020-05-03 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20200502_0323'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='checkbox_datetime',
            field=models.BooleanField(default=False, verbose_name='Checkbox'),
        ),
    ]
