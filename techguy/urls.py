from django.urls import path
# from .views import TechguyListView,TechguyDetailView, mail
from techguy import views

urlpatterns =[
    # path("", TechguyListView.as_view(), name="index"),
    # path("<slug:slug>/", TechguyDetailView.as_view(), name="TechguyDetailView"),
    path("mail/", views.mail, name="mail"),
    path('create', views.create),  
    path('show',views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
]