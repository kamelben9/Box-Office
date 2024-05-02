from django.db import models

# Create your models here.



class Film(models.Model):
    titre = models.CharField(max_length=500)
    distributeur = models.CharField(max_length=500)
    genre = models.CharField(max_length=100, default='Unknown')  # Add a default value here


    class Meta:
        db_table = 'dataset_model_ML'


class Acteurs_films(models.Model):
    film_id = models.ForeignKey(Film, on_delete=models.CASCADE)
    acteurs = models.CharField(max_length=500)

    class Meta:
        db_table = 'actors'


class Movies(models.Model):
    id = models.AutoField(primary_key=True)
    titre = models.CharField(max_length=500)
    image = models.URLField(max_length=200) 
    genre = models.CharField(max_length=100, default='Unknown')  # Add a default value here
    date = models.DateField()

    class Meta:
        db_table = 'movies'


class Prediction(models.Model):
    film = models.ForeignKey(Movies, on_delete=models.CASCADE)
    prediction = models.FloatField()
    titre = models.CharField(max_length=500)

    class Meta:
        db_table = 'prediction'
        
class Boxoffice(models.Model):
    film = models.ForeignKey(Movies, on_delete=models.CASCADE)
    boxoffice = models.IntegerField()

    class Meta:
        db_table = 'boxoffice'
