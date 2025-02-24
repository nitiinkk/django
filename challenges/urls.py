from django.urls import path
from . import views #from same folder import views

urlpatterns = [
    # /challenges/january
    path("january", views.index)
]