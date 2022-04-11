from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import PageSerializer, LinkSerializer
from .models import Page, Link

from .parser import get_links


class LinkList(generics.ListCreateAPIView):
    '''
    API endpoint that shows all links
    '''
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = [
            'find_url',
            'domain',
            'create_date',
            'update_date',
            'country',
            'is_dead',
            'a',
            'ns',
            'cname',
            'mx',
            'txt'
            ]

    def perform_create(self, serializer):
        serializer.save()


class LinkRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    '''
    API endpoint that show link
    '''
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class PageList(generics.ListCreateAPIView):
    '''
    API endpoint that shows all pages
    '''
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['page', 'find_urls']

    def perform_create(self, serializer):
        parsed_links = get_links(serializer.validated_data['page'])
        for links in parsed_links:
            urls = Link.objects.bulk_create([Link(find_url=links)])
            serializer.validated_data['find_urls'] = urls
        serializer.save()


class PageRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    '''
    API endpoint that show page
    '''
    queryset = Page.objects.all()
    serializer_class = PageSerializer
