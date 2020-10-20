from rest_framework import authentication
from homekjhkjh.models import HGFHJGJHG
from .serializers import HGFHJGJHGSerializer
from rest_framework import viewsets


class HGFHJGJHGViewSet(viewsets.ModelViewSet):
    serializer_class = HGFHJGJHGSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = HGFHJGJHG.objects.all()
