"""oms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from order import views as order_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',order_views.home,name='home'),
    path('login/',order_views.loginuser,name='login'),
    path('register/', order_views.registeruser,name='register'),
    path('logout/', order_views.logoutuser,name='logout'),
    path('profile/', order_views.userprofile,name='profile'),
    path('changepassword/', order_views.ChangePassword.as_view(template_name = 'order/changepassword.html'),name='changepassword'),

    path('products/',order_views.products,name='products'),
    path('createorder/',order_views.createOrder,name="createOrder"),
    path('updateorder/<str:pk>/',order_views.updateOrder,name='updateOrder'),
    path('deleteorder/<str:pk>/',order_views.deleteOrder,name='deleteOrder'),
    path('checkhome/',order_views.checkhome,name='dash'),
    path('searchorder/',order_views.search,name='searchorder'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)