from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('about-company/', include('aboutcomp.urls')),
    path('news/', include('news.urls')),
    path('product/', include('product.urls')),
    path('cart/', include('cart.urls')),
    path('register/', user_views.register, name='register'),
    path('accounts/profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
  
]
