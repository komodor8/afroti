from django.views import generic
from .models import Product, Market

class IndexSplashScreen(generic.ListView):
    template_name = 'personal/home.html'
    model = Product
    queryset = Product.objects.filter(categorie=1).order_by('order')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the markets
        context['markets'] = Market.objects.all()
        return context


class IndexFood(generic.ListView):
    template_name = 'personal/food.html'
    model = Product
    queryset = Product.objects.filter(categorie=3)


class IndexCake(generic.ListView):
    template_name = 'personal/cake.html'
    model = Product
    queryset = Product.objects.filter(categorie=2)
