from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from models import MovieReview, Movie, Actor, Director, MovieCategory
from forms import ActorForm, MovieForm, DirectorForm
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from serializers import ActorSerializer, MovieSerializer, DirectorSerializer



class MovieDetail(DetailView):
	model = Movie
	template_name = 'movie/movie_detail.html'

	def get_context_data(self, **kwargs):
		context = super(MovieDetail, self).get_context_data(**kwargs)
		#context['RATING_CHOICES'] = MovieReview.RATING_CHOICES
		return context

class MovieCreate(CreateView):
	''' Create Movie, use template form.html '''
	model = Movie
	template_name = 'form.html'
	form_class = MovieForm

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(MovieCreate, self).form_valid(form)

def MovieDelete(request, pk):
	'''Movie delete'''
	movie = get_object_or_404(Movie, pk=pk)
	movie.delete()
	return HttpResponseRedirect(reverse('imovie:movie_list', ))


class ActorDetail(DetailView):
	model = Actor
	template_name = 'actor/actor_detail.html'
	def get_context_data(self, **kwargs):
		context = super(ActorDetail, self).get_context_data(**kwargs)
		return context


class ActorCreate(CreateView):
	''' Create Actor, use template form.html '''
	model = Actor
	template_name = 'form.html'
	form_class = ActorForm

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(ActorCreate, self).form_valid(form)

def ActorDelete(request, pk):
	'''Actor delete'''
	actor = get_object_or_404(Actor, pk=pk)
	actor.delete()
	return HttpResponseRedirect(reverse('imovie:actor_list', ))


class DirectorDetail(DetailView):
	model = Director
	template_name = 'director/director_detail.html'


class DirectorCreate(CreateView):
	''' Create Director, use template form.html '''
	model = Director
	template_name = 'form.html'
	form_class = DirectorForm

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(DirectorCreate, self).form_valid(form)

def DirectorDelete(request, pk):
	'''Director delete'''
	director = get_object_or_404(Director, pk=pk)
	director.delete()
	return HttpResponseRedirect(reverse('imovie:director_list', ))

def category(request, pk):
	movie = get_object_or_404(Movie, pk=pk)
	category = MovieCategory(
		rating=request.POST['rating'],
		user=request.user,
		movie=movie)
	category.save()
	return HttpResponseRedirect(reverse('imovie:movie_detail', args=(movie.id,ea)))

def reviewM(request, pk):
	movie = get_object_or_404(Movie, pk=pk)
	reviews = MovieReview(
		rating=request.POST['rating'],
		comment=request.POST['comment'],
		user=request.user,
		movie=movie)
	reviews.save()
	return HttpResponseRedirect(reverse('imovie:movie_detail', args=(movie.id,)))


@api_view(['GET'])
def api_root(request, format=None):
    """
    The	entry endpoint of our API.
    """
    return Response({
        'actor': reverse('actor-list', request=request),
    })


class ActorListAPI(generics.ListCreateAPIView):
    """
    API	endpoint that represents a list	of	actor.
    """
    model = Actor
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    """
    API	endpoint that represents a single actor.
    """
    model = Actor
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class MovieListAPI(generics.ListCreateAPIView):
    """
    API	endpoint that represents a list	of	actor.
    """
    model = Movie
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    """
    API	endpoint that represents a single actor.
    """
    model = Movie
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class DirectorListAPI(generics.ListCreateAPIView):
    """
    API	endpoint that represents a list	of	movie.
    """
    model = Director
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class DirectorDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    """
    API	endpoint that represents a single director.
    """
    model = Director
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
