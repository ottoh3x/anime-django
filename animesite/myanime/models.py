from django.db import models
from django.urls import reverse


# Create your models here.



class AnimeCategory(models.Model):
    
    CATEGORI = (('Action', 'Action'),
                     ('Adventure', 'Adventure'),
                     ('Comedy', 'Comedy'),
                     ('Drama', 'Drama'),
                     ('Fantasy', 'Fantasy'),
                     ('Horror', 'Horror'),
                     ('Martial', 'Martial Arts'),
                     ('Mystery', 'Mystery'),
                     ('Super', 'Super Power'),
                     ('Supernatural', 'Supernatural'),
                     )
    category = models.CharField(max_length=200 , choices=CATEGORI)

    def __str__(self):
        return self.category
    

class Anime(models.Model):

    

    title_en = models.CharField(max_length=200 , blank=True , null=True)
    title_jp = models.CharField('Series Title (Japan)', max_length=100 , blank=True , null=True)
    description = models.TextField()
    slugy = models.SlugField()
    category = models.ForeignKey(AnimeCategory , on_delete=models.CASCADE , null = True , blank = True)
    image = models.ImageField(blank=True , null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    saison = models.IntegerField(null=True , blank = True)



    def __str__(self):
        return self.title_en
    

        


class Season(models.Model):
    title = models.ForeignKey(Anime , on_delete=models.CASCADE , null = True , blank = True)
    slug = models.SlugField(unique=True, help_text='Auto-generated from Title.')
    link = models.CharField(max_length=200, null = True , blank = True)
    category = models.ForeignKey(AnimeCategory , on_delete=models.CASCADE , null = True , blank = True)


    def __str__(self):
        return self.slug
    
    

class Episode(models.Model):

    anime = models.ForeignKey(Anime , on_delete=models.CASCADE , null = True , blank = True)
    episode_id = models.IntegerField(null = True , blank=True)
    url = models.CharField(max_length=200)


    def __str__(self):
        return self.anime.title_en + ' - ' +str(self.episode_id)
    class Meta:
        unique_together = ['anime', 'episode_id']



class Link(models.Model):
    url = models.CharField(max_length=200 , null=True,blank=True)
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.episode)
    
    