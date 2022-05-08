from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/delete', views.deleteView, name='delete'),
    path('<int:id>/detail', views.detailView, name='detail'),
    path('<int:id>/update', views.updateView, name='update'),
    path('signup', views.signupView, name='signup'),
    path('login', views.LoginView, name='login'),
    #path('success', views.success, name='success'),
    path('login_error', views.login_error, name='login_error'),
    path('logout', views.logout, name='logout'),
    #path('login', auth_views.LoginView.as_view(template_name='registration/login.html')),
    #path('login', auth_views.LoginView.as_view(redirect_authenticated_user=True)),
    path('userregistrationdone', views.userregistrationdoneView, name='userregistrationdone'),
]


