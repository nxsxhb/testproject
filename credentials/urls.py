from . import views
from store import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin


urlpatterns = [
    path('admin/',admin.site.urls),
    path('login/', views.login, name='login'),
    path('register/',views.register, name='register'),
    path('order/', views.order, name='order'),
    path('logout/',views.logout, name='logout'),
]

    