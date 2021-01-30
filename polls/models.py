from django.db import models

class Subject(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class University(models.Model):
	name = models.CharField(max_length=50)
	subjects = models.ManyToManyField(Subject)
	address = models.CharField(max_length=100)

	def __str__(self):
		return self.name

