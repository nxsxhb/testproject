from . import views
from store import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin

app_name = 'credentials'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('credentials/', include('credentials.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)