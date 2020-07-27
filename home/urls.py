from django.urls import path

from . import views
urlpatterns = [
    path('corehome',views.corehome,name='sign'),
    path('',views.sign,name='signin'),
        path('req',views.register,name='signin'),
    path('sign',views.sign,name='signin'),

    path('loginurl',views.loginurl,name='login'),
    path('login',views.login,name='login'),
    path('chatbox',views.chatbox,name='inbox'),
    path('profile',views.profile,name='profile'),
        path('search',views.search,name='sign'),
        path('core',views.corehome,name='home'),
        path('insertimage',views.insert,name='profileimage'),
            path('logout',views.login,name='logout'),
        path('score',views.scoremy,name='score'),
    path('query',views.query,name='query')







]