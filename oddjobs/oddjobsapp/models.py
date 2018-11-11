from django.db import models
from django.contrib.auth.models import User
from stream_django.activity import Activity

TOPIC_CHOICES = (
    ('kids','KIDS'),
    ('outdoor', 'OUTDOOR'),
    ('indoor','INDOOR'),
    ('volunteer','VOLUNTEER'),
    ('tutoring','TUTORING'),
    ('other', 'OTHER')
)

class Post(models.Model, Activity):
    created_at = models.DateTimeField(auto_now_add=True)
    topic = models.CharField(max_length=9, choices=TOPIC_CHOICES)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_text = models.CharField(max_length=2500)

    @property
    def activity_actor_attr(self):
        return self.author
