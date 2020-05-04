from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db import models
from django.utils import timezone

'''
    You have to run python manage.py syncdb (or python manage.py migrate if you use south - which you should)
    in order for changes to be applied to the database.
    https://stackoverflow.com/questions/22427388/django-db-utils-operationalerror-my-table-has-no-column-id-error
    1) python manage.py makemigrations  - alias = pmake
    2) python manage.py migrate  - alias = pmigrate
'''


# Created Model Post
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_time = models.TimeField(blank=True, null=True)
    published_date = models.DateField(blank=True, null=True)
    #published_date = models.DateTimeField(blank=True, null=True)
    checkbox_datetime = models.BooleanField('Checkbox', default=False)
    text = RichTextUploadingField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def expected_comments(self):
        return self.comments.filter(approved_comment=False)


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    text = RichTextUploadingField(blank=True, null=True, config_name='comment')

    def approve(self):
        self.approved_comment = True
        self.save()



    def __str__(self):
        return self.text
