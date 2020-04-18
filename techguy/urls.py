from django.urls import path
from .views import TechguyListView,TechguyDetailView, mail

urlpatterns =[
    path("", TechguyListView, name="index"),
    path("<int:pk>/", TechguyDetailView, name="TechguyDetailView"),
    path("mail/", mail, name="mail"),
]