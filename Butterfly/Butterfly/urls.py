from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD

from django.conf import settings

=======
from django.conf import settings
>>>>>>> 51281c64d59bfbf8341664d359d836dd76df6ad3
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('Butterfly_Home.urls'))
<<<<<<< HEAD
]
=======
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
>>>>>>> 51281c64d59bfbf8341664d359d836dd76df6ad3
