from django.urls import path

from . import views

urlpatterns = [
    path('formations/', views.formations, name='formations'),
    #path('upload_formations/', views.upload_formation, name='upload_formation'),
]
