from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from .views import user_list, user_detail

app_name = 'user'

urlpatterns = [
    path('', user_list, name='users'),
    path('<int:pk>/', user_detail, name='detail'),
    path('auth/accounts/', include('rest_registration.api.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]