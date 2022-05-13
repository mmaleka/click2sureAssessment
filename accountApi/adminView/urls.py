from . import views
from django.urls import path

app_name = 'adminView'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.csvReport, name='csv'),
    path('detail/', views.detail, name='detail'),
]