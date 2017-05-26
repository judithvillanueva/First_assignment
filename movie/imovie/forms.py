from django.forms import ModelForm
from models import Actor, Director, Movie


class ActorForm(ModelForm):
    class Meta:
        model = Actor
        fields = "__all__"
        exclude = ('user',)

class DirectorForm(ModelForm):
    class Meta:
        model = Director
        fields = "__all__"
        exclude = ('user',)

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"
        exclude = ('user',)
