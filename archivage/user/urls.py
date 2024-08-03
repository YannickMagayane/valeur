from django.urls import path
from .views import register, login_view,user_logout,UserListView,UserDeleteView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/',user_logout,name='logout'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('user/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),



]
