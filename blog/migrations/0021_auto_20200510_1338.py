# Generated by Django 3.0.4 on 2020-05-10 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20200510_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='checkbox_datetime',
            field=models.BooleanField(default=True),
        ),
    ]