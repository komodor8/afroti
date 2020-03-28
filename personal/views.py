from django.views import generic
from .models import Product

class IndexSplashScreen(generic.ListView):
    template_name = 'personal/home.html'
    model = Product
    queryset = Product.objects.filter(categorie=1)


class IndexFood(generic.ListView):
    template_name = 'personal/food.html'
    model = Product
    queryset = Product.objects.filter(categorie=3)


class IndexCake(generic.ListView):
    template_name = 'personal/cake.html'
    model = Product
    queryset = Product.objects.filter(categorie=2)
