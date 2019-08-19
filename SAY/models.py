from django.db import models

class Articel(models.Model):
	title = models.CharField(max_length = 120)
	post = models.TextField()
	photo = models.ImageField('Фото', upload_to = 'SAY/photos', default='', blank=True)
	date = models.DateTimeField()

	def __str__(self):
		return self.title
