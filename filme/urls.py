from django.urls import path
from .views import HomePage, HomeFilms, DetailFilm, SearchMovie

app_name='film'

urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('films', HomeFilms.as_view(), name='films'),
    path('search', SearchMovie.as_view(), name='search'),
    path('films/<int:pk>', DetailFilm.as_view(), name='detailfilm'),
]