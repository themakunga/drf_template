from rest_framework import mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from users.models import UserModel
from users.serializers import UserModelSerializer, UserRegisterSerializer

class UsersViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
    ):
    serializer_class = UserModelSerializer

    def get_permissions(self):
        permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]


    def create(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data, context={'request': self.request})
        serializer.validate(raise_exception=True)
        user = serializer.save()

        data = UserModelSerializer(user).data

        return Response(data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        queryset = UserModel.objects.filter(is_active=True)
        return queryset
