from rest_framework import generics
from .serializers import PageSerializer, LinkSerializer
from .models import Page, Link


class LinkList(generics.ListCreateAPIView):
    '''
    API endpoint that shows all links
    '''
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

    def perform_create(self, serializer):
        serializer.save()


class PageList(generics.ListCreateAPIView):
    '''
    API endpoint that shows all pages
    '''
    queryset = Page.objects.all()
    serializer_class = PageSerializer

    def perform_create(self, serializer):
        serializer.save()
