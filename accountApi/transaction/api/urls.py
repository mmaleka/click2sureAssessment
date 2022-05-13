from django.urls import path
from .views import transaction_list, transaction_detail, user_transaction

app_name = 'transaction'

urlpatterns = [
    path('', transaction_list, name='transactions'),
    path('<int:pk>/', transaction_detail, name='detail'),
    path('user_transaction/<int:user_id>/', user_transaction, name='user_transaction')
]