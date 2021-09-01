from django.urls import path
from Place import views

urlpatterns = [
    path("plan", views.goa, name="Goa"),
    path("planm", views.manali, name="Manali"),
   
]
