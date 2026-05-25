from django.urls import path
from .views import (
    bracelets_list,
    bracelet_detail,
    admin_dashboard,
    cart_view,
    add_to_cart,
    remove_from_cart,
    create_bracelet,
    update_bracelet,
    delete_bracelet,
)

urlpatterns = [
    path('', bracelets_list, name='bracelets_list'),
    path('cart/', cart_view, name='cart'),
    path('cart/add/<int:pk>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:pk>/', remove_from_cart, name='remove_from_cart'),
    path('manage/', admin_dashboard, name='admin_dashboard'),
    path('manage/add/', create_bracelet, name='add_bracelet'),
    path('manage/<int:pk>/edit/', update_bracelet, name='edit_bracelet'),
    path('manage/<int:pk>/delete/', delete_bracelet, name='delete_bracelet'),
    path('<int:pk>/', bracelet_detail, name='bracelet_detail'),
]
