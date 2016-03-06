from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.CharField(max_length=2000)
	pub_date = models.DateTimeField('date posted')

	def __str__(self):
		return str(self.author) + ' - ' + self.content

class Comment(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	content = models.CharField(max_length=2000)
	pub_date = models.DateTimeField('date posted')

	def __str__(self):
		return str(self.author) + ' - ' + self.content
