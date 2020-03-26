from django.views import generic


class IndexSplashScreen(generic.TemplateView):
    template_name = 'personal/home.html'


class IndexFood(generic.TemplateView):
    template_name = 'personal/food.html'


class IndexCake(generic.TemplateView):
    template_name = 'personal/cake.html'
