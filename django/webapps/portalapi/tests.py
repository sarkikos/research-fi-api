# This file is part of the research.fi API service
#
# Copyright 2019 Ministry of Education and Culture, Finland
#
# :author: CSC - IT Center for Science Ltd., Espoo Finland servicedesk@csc.fi
# :license: MIT
from django.test import SimpleTestCase
from django.urls import reverse
from . import views
from http import HTTPStatus

class ElasticsearchProxyViewTests(SimpleTestCase):
    base_url = '/portalapi/'

    def test_post_request_not_allowed_without_search(self):
        """When request HTTP method is POST and request URL does not contain '_search', it is rejected with status code 405 Method Not Allowed"""
        search_url = self.base_url + "/publication,person/"
        response = self.client.post(search_url)
        self.assertEquals(response.status_code,
                          HTTPStatus.METHOD_NOT_ALLOWED.value)

    def test_put_request_not_allowed(self):
        """When request HTTP method is PUT, it is rejected with status code 405 Method Not Allowed"""
        response = self.client.put(self.base_url)
        self.assertEquals(response.status_code,
                          HTTPStatus.METHOD_NOT_ALLOWED.value)

    def test_delete_request_not_allowed(self):
        """When request HTTP method is DELETE, it is rejected with status code 405 Method Not Allowed"""
        response = self.client.delete(self.base_url)
        self.assertEquals(response.status_code,
                          HTTPStatus.METHOD_NOT_ALLOWED.value)

    def test_patch_request_not_allowed(self):
        """When request HTTP method is PATCH, it is rejected with status code 405 Method Not Allowed"""
        response = self.client.patch(self.base_url)
        self.assertEquals(response.status_code,
                          HTTPStatus.METHOD_NOT_ALLOWED.value)