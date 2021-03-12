from django.urls import path
from django.conf.urls import url


from .views import index , signup , login , animedetails , episode , genre

urlpatterns = [
    path('', index , name = 'index'),
    path('signup/', signup , name = 'signup'),
    path('login/', login , name = 'login'),
    path('anime/<slug:slug>/' , animedetails , name ='animedetails'),
    path('Episode/<int:episode_id>/<slug:slugy>', episode , name = 'animewatching'),
    path('genre/<slug:name>/',genre , name='genre')
]
