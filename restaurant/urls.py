from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view(), name='menu-list'),
    path('menu/<int:id>', views.SingleMenuItemView.as_view(), name='menu-singleitem'),
    path('api-token-auth/', obtain_auth_token),
]