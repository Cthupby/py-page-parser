from rest_framework import generics
from .serializers import LinkSerializer
from .models import Link


class LinkList(generics.ListCreateAPIView):
    '''
    API endpoint that shows all links
    '''
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

    def perform_create(self, serializer):
        serializer.save()
