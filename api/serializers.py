from rest_framework import serializers
from .models import Link


class LinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Link
        fields = [
            'find_url', 'domain', 'create_date',
            'update_date', 'country', 'is_dead',
            'a', 'ns', 'cname', 'mx', 'txt'
            ]

    def get_links(self, link):
        return Link.objects.all()
