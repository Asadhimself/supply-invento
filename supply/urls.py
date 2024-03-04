from django.urls import path

from supply.views import (
    edit_order_view,
    login_view,
    home_view,
    logout_view,
    add_order_view,
    delete_order_view,
    manage_delete_order_view,
    manage_teachers_table,
    profile_view,
    section_view,
    sm_edit_view,
    st_edit_view,
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
    path("manage_table/<int:user_id>", manage_teachers_table, name="manage_table"),
    path("sm_edit/<int:order_id>", sm_edit_view, name="sm_edit"),
    path("st_edit/<int:order_id>", st_edit_view, name="st_edit"),
    path("manage_delete/<int:order_id>", manage_delete_order_view, name="manage_delete")
]

handler403 = "supply.views.custom_403"

