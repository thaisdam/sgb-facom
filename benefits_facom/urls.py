from django.contrib import admin
from django.urls import path
from benefits.views import concession_list_public
#benefits_facom/urls.py
#from django.conf.urls.i18n import i18n_patterns
from django.urls import include

urlpatterns = [
  #  path('i18n/', include('django.conf.urls.i18n')),
    path('concessoes/', concession_list_public, name='concession_public_list'),
    path('admin/', admin.site.urls),
    
]
