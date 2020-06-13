from django.urls import path
# from .views import TechguyListView,TechguyDetailView, mail
from techguy import views

urlpatterns =[
    # path("", TechguyListView.as_view(), name="index"),
    # path("<slug:slug>/", TechguyDetailView.as_view(), name="TechguyDetailView"),
    path("show", views.show, name='show'),
    path("mail/", views.mail, name="mail"),
    path('create', views.create),  
    path('show',views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
    path('cookie', views.showcookie, name="cookie"),
    path('visitcookie', views.visitcookie, name="visitcookie"),
    path('deletecookie', views.deletecookie, name="deletecookie"),

    # Sessions
    path('createsession/', views.create_session),
    path('accesssession', views.access_session),

    # order cruds
    path('customers/', views.customers, name="customers"),
    path('customers/create', views.create_customer, name="create_customer"),
    path('customers/detail/<str:pk>', views.customer_detail, name="detail_customer"),
    path('customers/update/<int:id>', views.update_customer, name="update_customer"),
    path('customers/delete/<int:id>', views.delete_customer, name="delete_customer"),

    path('products/', views.products, name="products"),
    path('orders/', views.orders, name="orders")
]