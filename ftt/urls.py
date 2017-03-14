from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.HealthView.as_view(), name='hello'),
]
