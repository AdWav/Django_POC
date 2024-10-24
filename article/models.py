from django.db import models

# Create your models here.
class Article(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    author = models.CharField(max_length=200, blank=True, default='')
    article = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='article', on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
             super(Article, self).save(*args, **kwargs)
