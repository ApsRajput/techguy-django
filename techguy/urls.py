from django.urls import path
# from .views import TechguyListView,TechguyDetailView, mail
from techguy import views

urlpatterns =[
    # path("", TechguyListView.as_view(), name="index"),
    # path("<slug:slug>/", TechguyDetailView.as_view(), name="TechguyDetailView"),
    path("show", views.show, name='show'),
    path("mail/", views.ContactForm.as_view(), name="mail"),
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

    # Order Crud Operations

    # Customer Operations
    path('customers/', views.customers, name="customers"),
    path('customers/create', views.create_customer, name="create_customer"),
    path('customers/detail/<str:pk>', views.customer_detail, name="detail_customer"),
    path('customers/update/<int:id>', views.update_customer, name="update_customer"),
    path('customers/delete/<int:id>', views.delete_customer, name="delete_customer"),

    # Product Operations
    path('products/', views.products, name="products"),
    path('products/create', views.create_product, name="create_product"),
    path('products/detail/<str:pk>', views.product_detail, name="detail_product"),
    path('products/update/<int:id>', views.update_product, name="update_product"),
    path('products/delete/<int:id>', views.delete_product, name="delete_product"),

    # Order Operations
    # path('orders/', views.orders, name="orders"),
    path("orders/", views.ListOrder.as_view(), name="orders"),
    path('orders/create', views.CreateOrder.as_view(), name="create_order"),
    path('orders/detail/<str:pk>', views.DetailOrder.as_view(), name="detail_order"),
    path('orders/update/<str:pk>', views.UpdateOrder.as_view(), name="update_order"),
    path('orders/delete/<int:pk>', views.DeleteOrder.as_view(), name="delete_order"),
]