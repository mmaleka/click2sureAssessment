from django.urls import path
from .views import account_list, account_detail#, user_account_list

app_name = 'account'

urlpatterns = [
    path('', account_list, name='account'),
    path('<int:pk>/', account_detail, name='detail'),
    # path('user_account_list/<int:user_id>/', user_account_list, name='user_account_list')
]