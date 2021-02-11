from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include

urlpatterns = [
    path('', include('calendar_index.urls')),
    path('admin/', admin.site.urls),
]
