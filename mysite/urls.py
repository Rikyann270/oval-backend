from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from main.views import (home_screen_view)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_screen_view),

    # rest_framework urls
    path('api/chicken/', include('chicken.api.urls', 'chicken_api')),
    path('api/account/', include('account.api.urls', 'account_api')),
    path('api/records/', include('records.api.urls', 'records_api')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)