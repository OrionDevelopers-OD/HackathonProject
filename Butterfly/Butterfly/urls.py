from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('Butterfly_Home.urls')),
    path('plants/', include('Butterfly_Plants.urls')),
<<<<<<< HEAD
=======
    path('seeds/', include('Butterfly_Seeds.urls')),
>>>>>>> bbf963b97b5cec8b639bf607b71368fa0332adf0
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
