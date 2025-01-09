from django.urls import path
from . import views

urlpatterns = [
    path("get_data/", views.get_values, name='get_value'),
    path("set_data/", views.set_values, name="set_value"),
    path("delete_data/<int:pk>/", views.delete_value, name='delete_value'),
    path("edit_data/<int:pk>/", views.edit_value, name='edit_value'),
]