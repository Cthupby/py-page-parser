from rest_framework import serializers
from .models import Page, Link


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = [
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


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ['page', 'find_urls']
