from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('Butterfly_Home.urls')),
    path('plants/', include('Butterfly_Plants.urls')),
    path('seeds/', include('Butterfly_Seeds.urls',)),
    # path('accounts/', include('socialdjango.urls',))
]
# + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
