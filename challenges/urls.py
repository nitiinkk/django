from django.urls import path
from . import views #from same folder import views

urlpatterns = [
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge) #dynamic path segment
]