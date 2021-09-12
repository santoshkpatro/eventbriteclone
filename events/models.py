from django.db import models
from django.contrib.auth.models import AnonymousUser, User


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    event_date = models.DateField(blank=True, null=True)
    event_time = models.TimeField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to='events/', blank=True, null=True)

    is_active = models.BooleanField(default=True)

    likes = models.ManyToManyField(User, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'events'

    def __str__(self) -> str:
        return self.title
