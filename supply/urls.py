from django.urls import path

from supply.views import login_view, home_view


urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login')
]
