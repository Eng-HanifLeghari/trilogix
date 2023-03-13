from django.urls import path
from . import views
urlpatterns = [
    path('trilogix/', views.trilogix_website),
]