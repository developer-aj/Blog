from django.db import models
from django.utils import timezone

from PIL import Image as PImage
from mysite.settings import MEDIA_ROOT

# Create your models here.
class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	subtitle = models.CharField(max_length=200, default="")
	text = models.TextField()
	image = models.ImageField(upload_to="images/", blank=True, null=True)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title
