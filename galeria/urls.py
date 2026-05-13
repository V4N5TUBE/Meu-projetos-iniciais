from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from galeria.views import index, imagem

urlpatterns = [
    path('', index, name='index'),
    path('imagem/', imagem, name='imagem'),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])