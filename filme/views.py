from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.

# def homepage(request):
#    return render(request, 'homepage.html')

class HomePage(TemplateView):
    template_name = "homepage.html"


# def homefilms(request):
#     context = {}
#     list_films = Filme.objects.all()
#     context['list_films'] = list_films
#     return render(request, 'homefilms.html', context)

class HomeFilms(ListView):
    template_name = "homefilms.html"
    model = Filme


class SearchMovie(ListView):
    template_name = "search.html"
    model = Filme

    def get_queryset(self):
        wordSearch = self.request.GET.get('q')
        if wordSearch:
            object_list = self.model.objects.filter(title__icontains=wordSearch)
            return object_list
        else:
            return None


class DetailFilm(DetailView):
    template_name = "detailfilm.html"
    model = Filme

    def get(self, request, *args, **kwargs):
        film = self.get_object()
        film.visualization += 1
        film.save()

        return super().get(request, *args, *kwargs)

    def get_context_data(self, **kwargs):
        context = super(DetailFilm, self).get_context_data(**kwargs)
        related_movies = self.model.objects.exclude(pk=self.get_object().pk).filter(category=self.get_object().category)[0:5]
        context["related_movies"] = related_movies

        return context