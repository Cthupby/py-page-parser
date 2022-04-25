from django.test import TestCase
from rest_framework.test import APIRequestFactory
from .models import Link
from .views import LinkList


class LinkTest(TestCase):
    '''
    We'll be testing with the LinkList view (class-based view).
    '''
    def setUp(self):
        self.factory = APIRequestFactory()
        self.post = Link.objects.create(find_url='https://losst.ru/')

    # For HTTP method GET
    def get(self):
        view = LinkList.as_view()
        request = self.factory.get('api/links/')
        response = view(request)

        self.assertEqual(response.status_code, 200)  # 200 = OK

    # For HTTP method POST
    def post(self):
        view = LinkList.as_view()

        # Generating the request
        request = self.factory.post('api/links/', {'find_url': 'https://losst.ru/'})

        response = view(request)
        expected = {'find_url': self.post.find_url}

        self.assertEqual(response.status_code, 201)  # 201 = created
        self.assertEqual(response.data, expected)
