from django.conf.urls import url
from .views import (
    LoginAPIView,
    TeamListAPIView,
    TeamCreateAPIView,
    UserMemberListAPIView,
    UserMemberCreateAPIView,
    ConfirmationEmailAPIView,
)

urlpatterns = [
    url(r'^login/$', LoginAPIView.as_view(), name='login'),
    url(r'^user_members/$', UserMemberListAPIView.as_view(), name='list'),
    url(r'^user_members/create/$', UserMemberCreateAPIView.as_view(), name='create'),
    url(r'^team/$', TeamListAPIView.as_view(), name='list'),
    url(r'^team/create/$', TeamCreateAPIView.as_view(), name='create'),
    url(r'^confirmation_email/(?P<token>.+)$', ConfirmationEmailAPIView.as_view(), name='confirmation_email'),
]
