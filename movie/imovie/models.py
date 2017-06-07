from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date


class Director(models.Model):
	name = models.TextField()
	birthday = models.DateField()
	biography = models.TextField(blank=True, null=True)
	user = models.ForeignKey(User, default=1)

	def __unicode__(self):
		return u"%s" % self.name

	def get_absolute_url(self):
		return reverse('imovie:director_detail', kwargs={'pk': self.pk})


class Actor(models.Model):
	name = models.TextField()
	birthday = models.DateField()
	biography = models.TextField(blank=True, null=True)
	city = models.TextField(max_length=50, null= True)
	country = models.TextField(max_length=50, null= True)
	state = models.TextField(max_length=50, null= True)
	user = models.ForeignKey(User, default=1)

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('imovie:actor_detail', kwargs={'pk': self.pk})


class Category(models.Model):
	CATEGORY_CHOICES = ((0, 'Undefined'), (1, 'Thriller'), (2, 'Comedy'), (3, 'Terror'), (4, 'Action'), (5, 'Romantic'), (6, 'Adventure'),
		(7, 'Sci-fi'), (8, 'Drama'), (9, 'Western'), (10, 'Animation'))
	category = models.PositiveSmallIntegerField('Category', blank=False, default=0, choices=CATEGORY_CHOICES)
	user = models.ForeignKey(User, default=1)


class Review(models.Model):
    ''' Review atributes '''
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)


class Movie(models.Model):
	name = models.TextField()
	year = models.IntegerField()
	overview = models.TextField(blank=True, null=True)
	user = models.ForeignKey(User, default=1)
	director = models.ForeignKey(Director)
	actors = models.ManyToManyField(Actor)

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('imovie:movie_detail', kwargs={'pk': self.pk})


class MovieReview(Review):
	movie = models.ForeignKey(Movie)


class MovieCategory(Category):
	movie = models.ForeignKey(Movie, related_name="cat")
