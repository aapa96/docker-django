from django.conf.urls import url, include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.documentation import include_docs_urls

from . import views
# from promo_api.views import categorias,usuarios
from rest_framework.routers import DefaultRouter

 

urlpatterns = [ 
    path('signup/', views.SignUp.as_view(), name='signup'),
]


urlpatterns += [
    url('api/', include('rest_framework.urls')),
]


urlpatterns = format_suffix_patterns(urlpatterns)