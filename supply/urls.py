from django.urls import path

from supply.views import edit_order_view, login_view, home_view, logout_view, add_order_view


urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('add_item/', add_order_view, name='add_order'),
    path('edit_order/<int:order_id>', edit_order_view, name='edit_order')
]
