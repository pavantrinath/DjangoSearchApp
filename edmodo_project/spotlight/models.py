from django.db import models

# Create your models here.
class Owner(models.Model):

    id = models.IntegerField(unique=True,primary_key=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    store_url = models.URLField()
    thumb_url= models.URLField()
    edmodo_url= models.URLField()



    def __str__(self):
        return str(self.id)


class Source(models.Model):

    id = models.IntegerField(unique=True,primary_key=True)
    currency = models.CharField(max_length=128)
    min_price = models.IntegerField(default=0)
    num_raters = models.IntegerField(default=0)
    creation_date = models.DateField()
    avg_rating = models.IntegerField(default=0)
    ##owner_id = models.IntegerField()
    seller_thumb_url = models.URLField()
    title = models.CharField(max_length=128)
    img_path = models.URLField()
    greads_review_url = models.URLField()
    owner = models.ForeignKey("Owner")

    def __str__(self):
     return str(self.title)


class Prod(models.Model):

   id = models.IntegerField(unique = True,primary_key=True)
   _index =  models.CharField(max_length=128)
   _type =  models.CharField(max_length=128)
   _score = models.IntegerField(default=0)
   source = models.ForeignKey("Source")

   def __str__(self):
    return str(self.id)

class Flag(models.Model):

   product = models.ForeignKey(Prod)
   Inappropriate =  models.CharField(max_length=12)
   Not_Helpful = models.CharField(max_length=12)
   Wrong_Tags = models.CharField(max_length=12)
   Spam = models.CharField(max_length=12)
