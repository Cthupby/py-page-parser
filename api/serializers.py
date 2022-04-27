from rest_framework import serializers
from .models import Page, Link


class LinkSerializer(serializers.ModelSerializer):
    '''
    Serializer for the link that the parser will find on the page
    '''
    class Meta:
        model = Link
        fields = [
            'id', 'find_url', 'domain', 'create_date', 'update_date',
            'country', 'is_dead', 'a', 'ns', 'cname', 'mx', 'txt'
            ]

        read_only_fields = [
            'id', 'domain', 'create_date', 'update_date', 'country',
            'is_dead', 'a', 'ns', 'cname', 'mx', 'txt'
            ]


class PageSerializer(serializers.ModelSerializer):
    '''
    Page serializer for parsing to find urls
    '''
    class Meta:
        model = Page
        fields = ['id', 'page', 'find_urls']

        read_only_fields = ['id', 'find_urls']
