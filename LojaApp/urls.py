from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns =[
    path('',index,name = 'index'),
    path('produto/<int:id>/',PageCompra,name = "PageCompra"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# suas outras urls aqui


 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)