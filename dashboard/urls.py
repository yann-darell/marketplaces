from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('buyer-dashboard/', views.buyer_dashboard, name='buyer_dashboard'),
    path('seller-dashboard/', views.seller_dashboard, name='seller_dashboard'),
    path('seller-products/', views.seller_products, name='seller_products'),
    path('review/<int:product_id>/', views.add_review, name='add_review'),
    path('notifications/', views.notifications, name='notifications'),
]
