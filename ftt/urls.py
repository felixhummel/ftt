from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.Entries.as_view(), name='home'),
    url(r'^health$', views.HealthView.as_view(), name='health'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^clock$', views.ClockView.as_view(), name='clock_start'),
]
