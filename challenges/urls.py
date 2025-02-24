from django.urls import path
from . import views #from same folder import views

urlpatterns = [
    path("<month>", views.monthly_challenge) #dynamic path segment
]