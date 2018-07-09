from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('signIn/', views.signIn, name='signIn'),
    path('postsign/', views.postsign, name='postsign'),
    path('logout/', views.logout, name='logout'),
    path('HMform/', views.HMform, name='HMform'),
    path('submitform',views.submitform, name='submitform')
]