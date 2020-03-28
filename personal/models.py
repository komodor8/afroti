from django.db import models


class Categorie(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name


class Product(models.Model):
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    main_product = models.BooleanField(default=False)
    menu_product = models.BooleanField(default=False)
    name = models.CharField(max_length=200, default='')
    subtitle = models.TextField(max_length=200, default='')
    description = models.TextField(max_length=200, default='')
    price = models.IntegerField(default=0)
    menu_name = models.CharField(max_length=200, default='')
    menu_description = models.TextField(max_length=200, default='')
    image_name = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.name


class Market(models.Model):
    name = models.CharField(max_length=200, default='')
    day = models.CharField(max_length=200, default='')
    location = models.CharField(max_length=200, default='')
    address = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.name
