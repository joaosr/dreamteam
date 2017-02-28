from rest_framework import serializers, viewsets
from dreamteam.core.models import UserMember

class UserMemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserMember
        fields = ('first_name', 'last_name', 'email', 'password')

# ViewSets define the view behavior.
class UserMemberViewSet(viewsets.ModelViewSet):
    queryset = UserMember.objects.all()
    serializer_class = UserMemberSerializer
