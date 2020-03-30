from django.views import generic
from .models import Product, Market


class IndexSplashScreen(generic.ListView):
    template_name = 'personal/home.html'
    model = Product
    queryset = Product.objects.filter(categorie=1).exclude(id=5).order_by('order')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add in the markets
        context['markets'] = Market.objects.all()
        context['best_seller'] = Product.objects.filter(id=5).first()
        return context


class IndexFood(generic.ListView):
    template_name = 'personal/food.html'
    model = Product
    queryset = Product.objects.filter(categorie=3).exclude(id=11).order_by('order')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['best_seller'] = Product.objects.filter(id=11).first()
        return context


class IndexCake(generic.ListView):
    template_name = 'personal/cake.html'
    model = Product
    queryset = Product.objects.filter(categorie=2).exclude(id=13).order_by('order')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['best_seller'] = Product.objects.filter(id=13).first()
        return context
