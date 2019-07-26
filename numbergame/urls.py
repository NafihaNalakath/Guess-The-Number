from django.conf.urls import url
from django.urls import path
from numbergame.views import guesss_number

urlpatterns = [
    url('^$', guesss_number, name='numbergame_url'),
]