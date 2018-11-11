from django.db import models
from django.contrib.auth.models import User
from stream_django.activity import Activity

class Post(models.Model, Activity):
    created_at = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_text = models.CharField(max_length=2500)

    @property
    def activity_actor_attr(self):
        return self.author
