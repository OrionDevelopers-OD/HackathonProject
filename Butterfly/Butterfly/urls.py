from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
=======
from django.conf import settings
>>>>>>> 2a25e1582811ef2a7640b2331e1bb46c4c399b11
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('Butterfly_Home.urls'))
<<<<<<< HEAD
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
=======
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
>>>>>>> 2a25e1582811ef2a7640b2331e1bb46c4c399b11
