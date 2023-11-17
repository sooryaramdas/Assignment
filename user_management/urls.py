
from django.urls import path
from .views import user_management_dashboard, user_details, account_creation, UserList

urlpatterns = [
    path('/', user_management_dashboard, name='dashboard'),
    path('user-details/', user_details, name='user_details'),
    path('account-creation/', account_creation, name='account_creation'),
    path('api/users/', UserList.as_view(), name='user-list'),
]
