from django.urls import path
from .views import maintainance_view, home_view

urlpatterns = [
    path('maintainance/', maintainance_view, name='maintainance'),
    path('', home_view, name='home'),
]