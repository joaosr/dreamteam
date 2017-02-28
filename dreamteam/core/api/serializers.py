from rest_framework.serializers import (
     CharField,
     EmailField,
     ModelSerializer,
     SerializerMethodField
     )
from django.core.exceptions import ValidationError
from dreamteam.core.models import UserMember, Team
from django.db.models import Q

class UserMemberSerializer(ModelSerializer):
    team = SerializerMethodField()
    # password = SerializerMethodField()
    class Meta:
        model = UserMember
        fields = ('first_name', 'last_name', 'email', 'password', 'team')
        extra_kwargs = {
            "password": {'write_only': True}
        }

    def create(self, validated_data):
        user_member = UserMember.objects.create(**validated_data)
        user_member.set_password(raw_password=user_member.password)
        user_member.save()
        return user_member

    def get_team(self, obj):
        if obj.team:
            return str(obj.team.name)
        else:
            return None

    def get_password(self, obj):
        return '#'*len(obj.password)



class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = ('name',)

class LoginSerialiser(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    email = EmailField(required=True, allow_blank=True)
    class Meta:
        model = UserMember
        fields = ('email', 'password', 'token')
        extra_kwargs = {
            "password": {'write_only': True}
        }

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        _user_member = None
        if not email:
            raise ValidationError("A email is required to login")

        user_member = UserMember.objects.filter(
            Q(email=email)
        ).distinct()

        if user_member.exists() and user_member.count() == 1:
            _user_member = user_member.first()
        else:
            raise ValidationError('This username/password is not valid')

        if _user_member:
            if not _user_member.check_password(password):
                raise ValidationError('Incorrect credential please try again.')

        data['token'] = "SOME RANDOM TOKEN"
        return data
