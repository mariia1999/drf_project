from django.urls import path
from users.apps import UsersConfig
from users.views import PaymentListAPIView, UserCreateAPIView, UserUpdateAPIView, UserListAPIView, PaymentCreateAPIView

app_name = UsersConfig.name

urlpatterns = [
    path("payment/", PaymentListAPIView.as_view(), name="payment_list"),
    path("payment/create/", PaymentCreateAPIView.as_view(), name="payment_create"),
    path("user/create/", UserCreateAPIView.as_view(), name="user_create"),
    path("user/", UserListAPIView.as_view(), name="user_list"),
    path("user/<int:pk>/update/", UserUpdateAPIView.as_view(), name="user_update"),
]



