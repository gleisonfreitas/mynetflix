from .models import Film

def recently_movies_list(request):
    movie_list = Film.objects.all().order_by('-creation_date')[0:8]
    if movie_list:
        most_recent_movie = movie_list[0]
    else:
        most_recent_movie = None
    return {'recently_movies_list': movie_list, 'most_recent_movie': most_recent_movie}

def top_movies_list(request):
    movie_list = Film.objects.all().exclude(visualization=0).order_by('-visualization')[0:8]
    return {'top_movies_list': movie_list}


def watched_movies_list(request):
    if not request.user.id:
        return []

    movie_list = request.user.movies_watched.all().order_by('-id')[0:8]
    return {'watched_movies_list': movie_list}

