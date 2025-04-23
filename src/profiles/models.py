from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    
    # Relationships
    bookmarked_articles = models.ManyToManyField('news.Article', blank=True, related_name='bookmarked_by')
    followed_categories = models.ManyToManyField('news.Category', blank=True, related_name='followers')
    followed_reporters = models.ManyToManyField('news.Reporter', blank=True, related_name='followers')
    
    # Preferences
    email_notifications = models.BooleanField(default=True)
    dark_mode = models.BooleanField(default=False)
    
    def __str__(self):
        return f'Profile for {self.user.username}'


class ReadingHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reading_history')
    article = models.ForeignKey('news.Article', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    read_completion = models.FloatField(default=0.0)  # 0.0 to 1.0 indicating reading progress
    
    class Meta:
        unique_together = ('user', 'article')
        ordering = ['-timestamp']
    
    def __str__(self):
        return f'{self.user.username} read {self.article.title}'
