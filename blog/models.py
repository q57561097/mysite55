from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=16, default='', blank=True)
    sex = models.IntegerField(default=0)
    phone = models.CharField(max_length=16, default='', blank=True)

    def __str__(self):
        return self.nickname

    def __unicode__(self):
        return self.nickname


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = UserProfile()
        profile.user = instance
        profile.save()

post_save.connect(create_user_profile, sender=User)
