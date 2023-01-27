from rest_framework.generics import CreateAPIView

from authentication.models import User
from authentication.serializers import CreateUserSerializer


class UserCreateView(CreateAPIView):
    model = User
    serializer_class = CreateUserSerializer
