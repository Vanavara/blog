from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Category(models.Model):
    name = models.CharField(max_length=255, unique = True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

#class Author(models.Model):

   #user = models.OneToOneField(User, on_delete=models.CASCADE)
   #user_rate = models.IntegerField(default=0)
   #full_name = models.CharField(max_length=255)

class Post(models.Model):
    article = 'СТ'
    news = 'НО'

    ARTICLE_NEWS = [
        (article, 'Статья'),
        (news, 'Новость'),
    ]

    title = models.CharField(max_length = 255)
    title_tag = models.CharField(max_length=2,choices=ARTICLE_NEWS,default=news)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.title + ' | ' + str(self.author)


    def get_absolute_url(self):
        return reverse('home')

# Create your models here.
