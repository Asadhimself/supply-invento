from django.urls import path

from supply.views import (
    edit_order_view,
    login_view,
    home_view,
    logout_view,
    add_order_view,
    delete_order_view,
    profile_view,
    section_view,
    sm_teachers_table,
)


urlpatterns = [
    path("", home_view, name="home"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("add_item/", add_order_view, name="add_order"),
    path("edit_order/<int:order_id>", edit_order_view, name="edit_order"),
    path("delete_order/<int:order_id>", delete_order_view, name="delete_order"),
    path("profile/<int:user_id>", profile_view, name="profile"),
    path("section/<str:pk>", section_view, name="section"),
    path("sm_table/<int:user_id>", sm_teachers_table, name="sm_table"),
]
