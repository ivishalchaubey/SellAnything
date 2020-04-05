from django.db import models

class rooms(models.Model):
	name = models.CharField(max_length=55)
	email = models.EmailField()
	price = models.IntegerField()
	discription = models.TextField(max_length=200)
	mobile = models.IntegerField()
	date = models.DateTimeField(auto_now=True)
	image = models.URLField()


	def __str__(self):
		return self.name

