from django.urls import path,include
from . import views
urlpatterns = [

    path('', views.base, name="base"),
    path('remove/<int:i>/', views.remove, name="remove"),
    path('update/<int:i>/', views.update, name="update"),
    
]
