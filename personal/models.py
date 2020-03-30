from django.db import models


class Categorie(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name


class Product(models.Model):
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    main_product = models.BooleanField(default=True)
    menu_product = models.BooleanField(default=True)
    name = models.CharField(max_length=200, null=True)
    subtitle = models.TextField(max_length=200, null=True)
    description = models.TextField(max_length=200, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    menu_name = models.CharField(max_length=200, null=True)
    menu_description = models.TextField(max_length=200, null=True)
    image_name = models.CharField(max_length=200, null=True)
    order = models.PositiveSmallIntegerField(default=999)

    def __str__(self):
        return self.name


class Market(models.Model):
    name = models.CharField(max_length=200)
    day = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name
