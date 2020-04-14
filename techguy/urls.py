from django.urls import path
from .views import TechguyListView,TechguyDetailView, mail

urlpatterns =[
    path("", TechguyListView.as_view(), name="index"),
    path("<int:pk>/", TechguyDetailView.as_view(), name="TechguyDetailView"),
    path("mail/", mail, name="mail"),
]