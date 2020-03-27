from django.db import models


class Categorie(models.Model):
    categorie_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.categorie_text

class Product(models.Model):
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    decription = models.CharField(max_length=200)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
