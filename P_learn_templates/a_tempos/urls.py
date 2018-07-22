from django.conf.urls import url
from a_tempos import views

# TEMPLATE TAGGING - needs to be app_name
app_name = 'a_tempos'

urlpatterns = [
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other_ka_naam'),
]
