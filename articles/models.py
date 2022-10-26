from django.db import models

# Create your models here.

class Article(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField(null=True, blank=True) 
	# DB에서 빈 값, front에서 빈 값.

	def __str__(self):
		return str(self.title)

    