
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView # new
urlpatterns = [
    path('admin/', admin.site.urls),
    path('appTest/', TemplateView.as_view(template_name='home.html'), name='home'),
    path('appTest/', include('django.contrib.auth.urls')), 
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('appTest/', include('appTest.urls'))
    
]
