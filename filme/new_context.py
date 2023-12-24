from .models import Filme

def recently_movies_list(request):
    movie_list = Filme.objects.all().order_by('-creation_date')[0:8]
    most_recent_movie = movie_list[0]
    return {'recently_movies_list': movie_list, 'most_recent_movie': most_recent_movie}

def top_movies_list(request):
    movie_list = Filme.objects.all().exclude(visualization=0).order_by('-visualization')[0:8]
    return {'top_movies_list': movie_list}