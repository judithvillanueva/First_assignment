from django.contrib.auth.models	import User, Group, Permission
from rest_framework import serializers
from models import Actor, Movie, Director


class ActorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actor
        fields = ('name', 'birthday', 'biography')

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ('name', 'year', 'overview')

class DirectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Director
        fields = ('name', 'birthday', 'biography')
