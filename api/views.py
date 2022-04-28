import asyncio
from rest_framework import generics
from rest_framework import filters
from rest_framework.exceptions import ValidationError
from dateutil.parser import parse
from urllib.parse import urlparse

from .serializers import PageSerializer, LinkSerializer
from .models import Page, Link

from .parser import get_links
from .domain_api import load_domain_data, domain_info


def parse_date(date):
    ''' Function to get date from domain API '''
    try:
        date = parse(date).date()
    except:
        date = None
    return date


class PageCreateList(generics.ListCreateAPIView):
    ''' API endpoint that return all pages and adding new ones '''
    queryset = Page.objects.all()
    serializer_class = PageSerializer

    def perform_create(self, serializer):
        ''' Parsing the page to get urls '''
        page = serializer.validated_data['page']
        parsed_links = get_links(page)
        ''' Getting more information from the API and adding urls '''
        for k, link in enumerate(parsed_links):
            url = urlparse(link).netloc.replace("www.", "")
            asyncio.run(load_domain_data(url))
            Link.objects.bulk_create([Link(
                find_url=link,
                domain=domain_info[k][0],
                create_date=parse_date(domain_info[k][1]),
                update_date=parse_date(domain_info[k][2]),
                country=str(domain_info[k][3]),
                is_dead=domain_info[k][4],
                a=str(domain_info[k][5]),
                ns=str(domain_info[k][6]),
                cname=str(domain_info[k][7]),
                mx=str(domain_info[k][8]),
                txt=str(domain_info[k][9]),
                )], ignore_conflicts=True)
        find_urls = Link.objects.filter(find_url__in=parsed_links).values_list('id', flat=True)
        domain_info.clear()
        try:
            serializer.save(page=page.replace("www.", ""), find_urls=find_urls)
        except ValidationError:
            raise ValidationError('This page already exist in this table.')


class PageLinksList(generics.ListCreateAPIView):
    ''' API endpoint that returns all links found on the page '''
    serializer_class = LinkSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['domain', 'country', 'is_dead', 'a', 'ns', 'cname', 'mx', 'txt']
    ordering_fields = ['domain', 'country', 'create_date', 'update_date']

    def get_queryset(self):
        page = self.kwargs['pk']
        return Page.objects.get(id=page).find_urls.all()

    def perform_create(self, serializer):
        serializer.save()


class PageRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    ''' API endpoint for editing or deleting a page '''
    queryset = Page.objects.all()
    serializer_class = PageSerializer

    def perform_create(self, serializer):
        serializer.save()


class LinkRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    ''' API endpoint for editing or deleting a link '''
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
