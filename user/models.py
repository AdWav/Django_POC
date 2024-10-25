from django.db import models

# Create User model here
class User(models.Model):
    user = models.CharField(max_length=30, blank=True, default='')
    username = models.CharField(max_length=30, blank=False, default=user)

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

