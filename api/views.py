from rest_framework import generics
from .serializers import PageSerializer, LinkSerializer
from .models import Page, Link

from .parser import get_links


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
        for link in get_links(serializer.validated_data['page']):
            url = Link.objects.bulk_create([Link(find_url=link)])
            serializer.validated_data['find_urls'] = url
        serializer.save()
