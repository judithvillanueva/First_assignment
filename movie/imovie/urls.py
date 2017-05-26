from django.conf.urls import url, patterns, include
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from django.views.generic.base import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns
from forms import ActorForm, MovieForm, DirectorForm
from models import Director, Movie, Actor,\
					MovieReview, MovieCategory, Review
from views import MovieDetail, ActorDetail, review,\
					DirectorDetail, ActorListAPI, ActorDetailAPI,\
					ActorCreate, ActorDelete, MovieDelete, MovieCreate,\
					DirectorDelete, DirectorCreate, DirectorListAPI, \
					DirectorDetailAPI, MovieListAPI, MovieDetailAPI


urlpatterns = [

	# Home page
	url(r'^$', TemplateView.as_view(template_name="principal.html"), name="Principal"),

	# Movies list
	url(r'^movie/$', ListView.as_view(
			queryset=Movie.objects.filter().order_by('user')[:5],
			context_object_name='latest_movie_list',
			template_name='movie/movie_list.html'),
		name='movie_list'),

	# Movies detail
	url(r'^movie/(?P<pk>\d+)/$', MovieDetail.as_view(
			model=Movie,
			template_name='movie/movie_detail.html'),
		name='movie_detail'),

	# Movie create
	url(r'^movie/create/$', MovieCreate.as_view(), name='movie_create'),

	# Movie edit
	url(r'^movie/(?P<pk>\d+)/edit/$', UpdateView.as_view(
		model=Movie,
		template_name='form.html',
		form_class=MovieForm),
		name='movie_edit'),

	# Movie delete
	url(r'^movie/(?P<pk>\d+)/delete/$', MovieDelete, name='movie_delete'),


	# Actor list
	url(r'^actor/$', ListView.as_view(
			queryset=Actor.objects.filter().order_by('user')[:5],
			context_object_name='latest_actor_list',
			template_name='actor/actor_list.html'),
		name='actor_list'),

	# Actor detail
	url(r'^actor/(?P<pk>\d+)/$', ActorDetail.as_view(
			model=Actor,
			template_name='actor/actor_detail.html'),
		name='actor_detail'),

	# Actor create
	url(r'^actor/create/$', ActorCreate.as_view(),
		name='actor_create'),

	# Actor edit
	url(r'^actor/(?P<pk>\d+)/edit/$', UpdateView.as_view(
		model=Actor,
		template_name='form.html',
		form_class=ActorForm),
		name='actor_edit'),

	# Actor delete
	url(r'^actor/(?P<pk>\d+)/delete/$', ActorDelete,
		name='actor_delete'),

	# Director list
	url(r'^director/$', ListView.as_view(
			queryset=Director.objects.filter().order_by('user')[:5],
			context_object_name='latest_director_list',
			template_name='director/director_list.html'),
		name='director_list'),

	# Director detail
	url(r'^director/(?P<pk>\d+)/$', DirectorDetail.as_view(
			model=Director,
			template_name='director/director_detail.html'),
		name='director_detail'),

	# Director create
	url(r'^director/create/$', DirectorCreate.as_view(), name='director_create'),

	# Director edit
	url(r'^director/(?P<pk>\d+)/edit/$', UpdateView.as_view(
		model=Director,
		template_name='form.html',
		form_class=DirectorForm),
		name='director_edit'),

	# Director delete
	url(r'^director/(?P<pk>\d+)/delete/$', DirectorDelete, name='director_delete'),



	# RESTful API
	url(r'^api/actor/$',ActorListAPI.as_view(), name='actor-list'),
	url(r'^api/actor/(?P<pk>\d+)/$', ActorDetailAPI.as_view(), name='actor-detail'),

	url(r'^api/director/$',DirectorListAPI.as_view(), name='director-list'),
	url(r'^api/director/(?P<pk>\d+)/$', DirectorDetailAPI.as_view(), name='director-detail'),

	url(r'^api/movie/$',MovieListAPI.as_view(), name='movie-list'),
	url(r'^api/movie/(?P<pk>\d+)/$', MovieDetailAPI.as_view(), name='movie-detail'),

]

# Format	suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])


#	Default	login/logout	views
urlpatterns += patterns('', url(r'^api-auth/', include('rest_framework.urls', namespace = 'rest_framework'))
)
