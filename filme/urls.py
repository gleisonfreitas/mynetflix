from django.urls import path
from .views import HomePage, HomeFilms, DetailFilm

app_name='film'

urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('films', HomeFilms.as_view(), name='films'),
    path('films/<int:pk>', DetailFilm.as_view(), name='detailfilm'),
]