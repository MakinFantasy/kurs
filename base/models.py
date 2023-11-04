from django.db import models
from django.utils import timezone


class Category(models.Model):
	title = models.CharField(max_length=100)
	date_created = models.DateTimeField(timezone.now())
	image = models.ImageField(upload_to='images/')

	class Meta:
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.title


class Tag(models.Model):
	title = models.CharField(max_length=100)
	date_created = models.DateTimeField(timezone.now())

	class Meta:
		verbose_name_plural = "Tags"

	def __str__(self):
		return self.title


class Product(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	image = models.ImageField(upload_to='images/')
	date_created = models.DateTimeField(timezone.now())
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	tags = models.ManyToManyField(Tag)
	price = models.IntegerField()

	class Meta:
		verbose_name_plural = "Products"

	def __str__(self):
		return self.title


class Comment(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	email = models.EmailField(max_length=254)
	status = models.BooleanField(default=False)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = "Comments"

	def __str__(self):
		return self.title


class Subscriber(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(unique=True, max_length=200)
	date_created = models.DateTimeField(null=True, blank=True)
	date_updated = models.DateTimeField(null=True, blank=True)

	def __str__(self):
		return self.email
