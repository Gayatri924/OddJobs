from django.db import models
from django.contrib.auth.models import User
from stream_django.activity import Activity
#from stream_django.enrich import Enrich
#from stream_django.feed_manager import feed_manager
#from oddjobs import settings

#<<<<<<< HEAD
class Post(models.Model,Activity):
    created_at = models.DateTimeField(auto_now_add=True)
    #topic = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    text=models.CharField(max_length=160)
    #feed_manager.get_user_feed(user_id)
    #timeline = feed_manager.get_news_feeds(user_id)['timeline']
    #timeline_aggregated = feed_manager.get_news_feeds(user_id)['timeline_aggregated']
    #notification_feed = feed_manager.get_notification_feed(user_id)



    #enricher = Enrich()
    #feed = feed_manager.get_feed('timeline', request.user.id)
    #activities = feed.get(limit=25)['results']
    #enriched_activities = enricher.enrich_activities(activities)
"""=======
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
>>>>>>> master"""

"""@property
    def activity_actor_attr(self):
        return self.user
"""
