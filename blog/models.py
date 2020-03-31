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
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

