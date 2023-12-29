from django.shortcuts import render, redirect, reverse
from .models import Film
from .forms import CreateAccountForm
from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# def homepage(request):
#    return render(request, 'homepage.html')

class HomePage(TemplateView):

    template_name = "homepage.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('film:films')
        else:
            return super().get(request, *args, *kwargs)



# def homefilms(request):
#     context = {}
#     list_films = Filme.objects.all()
#     context['list_films'] = list_films
#     return render(request, 'homefilms.html', context)

class HomeFilms(LoginRequiredMixin, ListView):
    template_name = "homefilms.html"
    model = Film


class SearchMovie(LoginRequiredMixin, ListView):
    template_name = "search.html"
    model = Film

    def get_queryset(self):
        wordSearch = self.request.GET.get('q')
        if wordSearch:
            object_list = self.model.objects.filter(title__icontains=wordSearch)
            return object_list
        else:
            return None


class DetailFilm(LoginRequiredMixin, DetailView):
    template_name = "detailfilm.html"
    model = Film

    def get(self, request, *args, **kwargs):
        film = self.get_object()
        film.visualization += 1
        film.save()
        
        user = request.user
        user.movies_watched.add(film)

        return super().get(request, *args, *kwargs)

    def get_context_data(self, **kwargs):
        context = super(DetailFilm, self).get_context_data(**kwargs)
        related_movies = self.model.objects.exclude(pk=self.get_object().pk).filter(category=self.get_object().category)[0:5]
        context["related_movies"] = related_movies

        return context

class ProfileEdit(LoginRequiredMixin, TemplateView):
    template_name = "profileedit.html"


class CreateAccount(FormView):
    template_name = "createAccount.html"
    form_class = CreateAccountForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('film:login')

