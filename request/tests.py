from django.test import TestCase
from django.test import RequestFactory, TestCase
from .views import get_Request, RequestListView, all_requests

# Create your tests here.
from django.contrib.auth.models import User

class RequestViewsTestCase(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret')

    def test_get_request(self):
        request = self.factory.get('')
        request.user = self.user
        response = get_Request(request)
        self.assertEqual(response.status_code, 200)

    def test_request_list(self):
        request = self.factory.get('list/')
        request.user = self.user
        response = RequestListView.as_view()(request)
        self.assertEqual(response.status_code, 200)
    
    def test_all_requests(self):
        request = self.factory.get('allrequests/')
        request.user = self.user
        response = all_requests(request)
        self.assertEqual(response.status_code, 200)
    
 
