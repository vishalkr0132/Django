from Home import views
from django.conf import settings
from django.urls import include, path
from django.urls import path
from .views import login_user

urlpatterns = [
    path('',views.index, name='home'),
    path('offer',views.offer, name='offer'),
    path('order',views.order, name='order'),
    path('payment',views.payment, name='payment'),
    path('swiggy',views.swiggy, name='swiggy'),
    path('admin_index',views.admin_index, name='admin_index'),
    path('login', views.login_user, name='login'),
    path('admin_panda', views.admin_panda, name='admin_panda'),
    path('admin_swigy', views.admin_swigy, name='admin_swigy'),
    path('admin_zomat', views.admin_zomat, name='admin_zomat'),

]