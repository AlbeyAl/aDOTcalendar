from django.urls import path, include
from calendar_index import views

app_name = 'index'

urlpatterns = [
    path('<slug:calendar_name>/<int:year>/<int:month>/<int:day>', views.calendar)
]
