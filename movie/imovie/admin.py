from django.contrib import admin
import models
# Register your models here.

admin.site.register(models.Director)
admin.site.register(models.Actor)
admin.site.register(models.Category)
admin.site.register(models.Review)
admin.site.register(models.Movie)
admin.site.register(models.MovieReview)
admin.site.register(models.MovieCategory)
