from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
# Post is my object, with the properties and their data types defined as follows
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # Be sure to indent for your methods so that those are part of the object
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title