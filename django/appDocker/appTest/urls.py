from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.documentation import include_docs_urls

from . import views
# from promo_api.views import categorias,usuarios
from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register(r'CategoriaUno', CategoriaUnoList)
# router.register(r'CategoriaDos', CategoriaDosList)
# router.register(r'CategoriaTres', CategoriaTresList)


urlpatterns = [
    # url(r'^docs/', include_docs_urls(title='Test API')),
    
    # url(r'^categoriaUno/$', categorias.CategoriaUnoList.as_view()),
    
    # url(r'^categoriaDos/$', categorias.CategoriaDosList.as_view()), 
]


urlpatterns += [
    url('api/', include('rest_framework.urls')),
]


urlpatterns = format_suffix_patterns(urlpatterns)