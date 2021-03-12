from django.shortcuts import render , get_object_or_404 , get_list_or_404
from .models import *

# Create your views here.


def index(request):

    episode=Episode.objects.all()
    animes = Anime.objects.all()
    zipped_data = zip(episode, animes)
    category = AnimeCategory.objects.all()


    context = {'episode':episode,'animes' : animes,
    
    'zipped_data':zipped_data,
    'category':category
    }
    return render (request , 'base.html' ,context)


def signup(request):

    context = {}
    return render(request, 'signup.html' , context)    


def login(request):

    context = {}
    return render(request, 'login.html' , context)  


def animedetails(request , slug):
    
    get_anime = Anime.objects.filter(slugy = slug)
    episodes = Episode.objects.all()
    anime = Anime.objects.get(slugy=slug)
    ep_list = Episode.objects.filter(anime = anime)
    all_ep = ep_list.all()

    context = {'animes' : get_anime
    , 'episodes':episodes,
    'all' : all_ep,
    'anime':anime,}
    return render(request, 'anime-details.html' , context) 


   

def episode(request, episode_id , slugy):


    anime = Anime.objects.get(slugy=slugy)
    ep_list = Episode.objects.filter(anime = anime)
    all_ep = ep_list.all()
    ep_video = Episode.objects.get(anime = anime , episode_id=episode_id)
    get_video = Link.objects.filter(episode_id = ep_video)


    context = {'episode': ep_list,
    'anime':anime,
    'all' : all_ep,
    'ep':ep_video,
    'video':get_video
    }
    return render(request, 'anime-watching.html', context)


def genre(request , name):

    get_cat = AnimeCategory.objects.get(category = name)
    animecat = Anime.objects.filter(category = get_cat)

    context={'all_cat':animecat}
    return render(request , 'genre.html' , context)    