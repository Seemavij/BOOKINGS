from . import views
from django.urls import path

urlpatterns = [
    path('bookings', views.PostList.as_view(), name='home'),
]