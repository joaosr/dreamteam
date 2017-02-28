from rest_framework.generics import (ListAPIView, CreateAPIView)

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    )

from dreamteam.core.models import UserMember, Team
from dreamteam.core.api.serializers import (
    UserMemberSerializer,
    TeamSerializer,
    LoginSerialiser,
    )


class UserMemberListAPIView(ListAPIView):
    queryset = UserMember.objects.all()
    serializer_class = UserMemberSerializer

class UserMemberCreateAPIView(CreateAPIView):
    queryset = UserMember.objects.all()
    serializer_class = UserMemberSerializer

class TeamListAPIView(ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamCreateAPIView(CreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class LoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerialiser

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = LoginSerialiser(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
