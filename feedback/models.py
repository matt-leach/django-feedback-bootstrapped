from django.conf import settings
from django.db import models


class Feedback(models.Model):
    text = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="feedback")
    url = models.URLField()
    time = models.DateTimeField(auto_now_add=True)
