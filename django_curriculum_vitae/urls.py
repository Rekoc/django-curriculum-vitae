from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from cv_app import urls as cv

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'', include(cv))
]
