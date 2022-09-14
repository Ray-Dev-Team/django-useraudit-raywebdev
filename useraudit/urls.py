from django.urls import path
from .views import reactivate_user

app_name = "useraudit"

urlpatterns = [
    path('reactivate/<int:user_id>/', reactivate_user, name="reactivate_user"),
]
