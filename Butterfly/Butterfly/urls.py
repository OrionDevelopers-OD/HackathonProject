from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('home/', include('Butterfly_Home.urls')),
    path('cart/', include('shop.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
=======
    path('home/', include('Butterfly_Home.urls'))
]
>>>>>>> 37af6d780a515615af899f4fab7c343b59001662
