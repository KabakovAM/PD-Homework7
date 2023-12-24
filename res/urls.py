from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('main/', views.five_recipe, name='main'),
    path('recipe/<int:pk>/', views.one_recipe, name='recipe'),
    path('register/', views.register, name='register'),
    path('login/', views.NewLoginView.as_view(template_name= 'res/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='res/logout.html'), name='logout'),
    path('new_recipe/', views.new_recipe, name='new_recipe'),
    path('update_recipe/', views.update_recipe, name='update_recipe'),
    path('all_recipe/', views.all_recipe, name='all_recipe'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)