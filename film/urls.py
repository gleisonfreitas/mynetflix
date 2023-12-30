from django.urls import path, reverse_lazy
from .views import HomePage, HomeFilms, DetailFilm, SearchMovie, ProfileEdit, CreateAccount
from django.contrib.auth import views as auth_view

app_name='film'
urlpatterns = [
    path(
        '',
        HomePage.as_view(),
        name='homepage'
    ),
    path(
        'login',
        auth_view.LoginView.as_view(template_name='login.html'),
        name='login'
    ),
    path(
        'logout',
        auth_view.LogoutView.as_view(template_name='logout.html'),
        name='logout'
    ),
    path(
        'films',
        HomeFilms.as_view(),
        name='films'
    ),
    path(
        'search',
        SearchMovie.as_view(),
        name='search'
    ),
    path(
        'films/<int:pk>',
        DetailFilm.as_view(),
        name='detailFilm'),
    path(
        'profileEdit/<int:pk>',
        ProfileEdit.as_view(),
        name='profileEdit'
    ),
    path(
        'createAccount',
        CreateAccount.as_view(),
        name='createAccount'
    ),
    path(
        'changePassword',
        auth_view.PasswordChangeView.as_view(template_name='profileedit.html',
                                             success_url=reverse_lazy('film:films')),
        name='changePassword'
    ),
]

