from users.models import Payment, User
from users.serializers import PaymentSerializer, UserSerializer


class UserCreateApiView(CreateApiView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserListApiView(ListApiView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateApiView(UpdateApiView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PaymentListAPIView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('paid_lesson', 'paid_course', 'payment_type',)
    ordering_fields = ('date',)


class PaymentCreateAPIView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    