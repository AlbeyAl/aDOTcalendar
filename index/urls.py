from django.urls import path, include
from index import views

app_name = 'index'

urlpatterns = [
    path('calender/', views.to_error_out)
]
