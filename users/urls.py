from django.urls import path
from users.apps import UsersConfig
from users.views import PaymentListAPIView, UserCreateApiView, UserUpdateApiView, UserListApiView, PaymentCreateAPIView

app_name = UsersConfig.name

urlpatterns = [
    path("payment/", PaymentListApiView.as_view(), name="payment_list"),
    path("payment/create/", PaymentCreateApiView.as_view(), name="payment_create"),
    path("user/create/", UserCreateApiView.as_view(), name="user_create"),
    path("user/", UserListApiView.as_view(), name="user_list"),
    path("user/<int:pk>/update/", UserUpdateApiView.as_view(), name="user_update"),
]



