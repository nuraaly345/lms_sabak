from unicodedata import name
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', homepage, name='homepage'),
    path('lessons', index, name='home'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('addpage/', addpage, name='add_page'),
    path('register/', register, name='register'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('login/', login_user, name='login'),
    path('edit/', edit, name='edit'),
    path('profile/', profile, name='profile'),
    path('<int:pk>', NewsDetailView.as_view(), name='lesson-detail'),
    path('<int:pk>/update', NewsUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', NewsDeleteView.as_view(), name='delete'),
]
