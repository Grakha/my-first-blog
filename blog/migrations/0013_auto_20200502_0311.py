# Generated by Django 3.0.4 on 2020-05-01 23:11

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_post_comment_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comment_text',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
