
from django.contrib import admin
from django.urls import path,include
from  . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first/', include('first_app.urls')),
    path('l/', views.index_13),
    path('m/', views.index_14),
    path('n/', views.index_15),
]
