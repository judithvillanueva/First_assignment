from django.conf.urls import url
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from django.views.generic.base import TemplateView
from models import Director, Movie, Actor,\
					MovieReview, MovieCategory, Review
from views import MovieDetail, MovieList, ActorList, ActorDetail, review,\
					DirectorList, DirectorDetail

urlpatterns = [

	# Home page
	url(r'^$', TemplateView.as_view(template_name="imovie/principal.html"), name="Principal"),

	# Movies list
	url(r'^movie/$', MovieList.as_view(
			context_object_name='latest_movie_list',
			template_name='imovie/movie_list.html'),
		name='movie_list'),

	# Movies detail
	url(r'^movie/(?P<pk>\d+)/$',
		MovieDetail.as_view(
			model=Movie,
			template_name='imovie/movie_detail.html'),
		name='movie_detail'),


	# Actor list
	url(r'^actor/$',
		ActorList.as_view(
			context_object_name='latest_actor_list',
			template_name='imovie/actor_list.html'),
		name='actor_list'),

	# Actor detail
	url(r'^actor/(?P<pk>\d+)/$',
		ActorDetail.as_view(
			model=Actor,
			template_name='imovie/actor_detail.html'),
		name='actor_detail'),

	# Director list
	url(r'^director/$',
		DirectorList.as_view(
			context_object_name='latest_director_list',
			template_name='imovie/director_list.html'),
		name='director_list'),

	# Director detail
	url(r'^director/(?P<pk>\d+)/$',
		DirectorDetail.as_view(
			model=Director,
			template_name='imovie/director_detail.html'),
		name='director_detail'),
]
