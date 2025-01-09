from django.urls import path
from . import views

urlpatterns = [
    path("get_data/", views.get_values, name='ip_get_values'),
    path("set_data/", views.set_values, name="ip_set_values"),
    path("delete_data/<int:pk>/", views.delete_value, name='ip_delete'),
    path("update_data/<int:pk>", views.edit_value, name='ip_edit'),
]