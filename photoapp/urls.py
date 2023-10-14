from django.urls import path
from . import views

urlpatterns = [
    path('',views.ViewGallary, name='gallary'),
    path('images/<str:pk>/',views.ViewImages, name='image'),
    path('add/',views.addNewPhotos, name='add'),

]