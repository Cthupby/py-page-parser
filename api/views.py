from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from dateutil.parser import parse
from urllib.parse import urlparse

from .serializers import PageSerializer, LinkSerializer
from .models import Page, Link

from .parser import get_links
from .domainsdb_info import *


def parse_date(date):
    '''
    Function that can parse date
    '''
    try:
        date = parse(date).date()
    except:
        date = None
    return date


class LinkList(generics.ListCreateAPIView):
    '''
    API endpoint that shows all links
    '''
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['find_url', 'domain', 'country', 'is_dead']

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
        for pk, link in enumerate(parsed_links):
            '''
            Start async function for load domain data
            '''
            url = urlparse(link).netloc.replace("www.", "")
            asyncio.run(load_domain_data(url))
            urls = Link.objects.bulk_create([Link(
                find_url=link,
                domain=domain_info[pk][0],
                create_date=parse_date(domain_info[pk][1]),
                update_date=parse_date(domain_info[pk][2]),
                country=str(domain_info[pk][3]),
                is_dead=domain_info[pk][4],
                a=str(domain_info[pk][5]),
                ns=str(domain_info[pk][6]),
                cname=str(domain_info[pk][7]),
                mx=str(domain_info[pk][8]),
                txt=str(domain_info[pk][9]),
                )])
            serializer.validated_data['find_urls'] = urls
        serializer.save()


class PageRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    '''
    API endpoint that show page
    '''
    queryset = Page.objects.all()
    serializer_class = PageSerializer
