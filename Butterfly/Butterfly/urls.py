from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('Butterfly_Home.urls')),
<<<<<<< HEAD
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
=======
]
>>>>>>> 2233944291354dfca66f498fc4d9cb15ce520ab0
