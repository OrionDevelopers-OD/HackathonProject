from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('Butterfly_Home.urls')),
<<<<<<< HEAD
    path('cart/', include('shop.urls')),
]
=======
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
>>>>>>> cdda334a70aeff0b40dd115e6f59aaef1c475399
