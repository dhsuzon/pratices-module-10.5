from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('a/',views.index_2),
    path('b/',views.index_3),
    path('c/',views.index_4),
    path('d/',views.index_5),
    path('d/',views.index_6),
    path('e/',views.index_7),
    path('f/',views.index_8),
    path('g/',views.index_9),
    path('h/',views.index_10),
    path('i/',views.index_11),
    path('j/',views.index_12),
    path('k/',views.index_of),
   
]
