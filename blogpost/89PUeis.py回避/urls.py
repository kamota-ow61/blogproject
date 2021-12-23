from django.contrib import admin
from django.urls import path
from .views import BlogList

urlpatterns = [
    path('admin/', admin.site.urls),
]

