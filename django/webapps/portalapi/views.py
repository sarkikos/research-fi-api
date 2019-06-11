# This file is part of the research.fi API service
#
# Copyright 2019 Ministry of Education and Culture, Finland
#
# :author: CSC - IT Center for Science Ltd., Espoo Finland servicedesk@csc.fi
# :license: MIT
from django.http import HttpResponseNotAllowed, HttpResponse
from django.conf import settings
from http import HTTPStatus
from revproxy.views import ProxyView
import re


class ElasticsearchProxyView(ProxyView):
    """
    Proxies GET request to Elasticsearch.
    Proxies POST request to Elasticsearch when the POST request URL contains "_search".
    All other HTTP requests are blocked and responded with status code 405 Method Not Allowed.
    """

    def dispatch(self, request, *args, **kwargs):
        """
        Extend ProxyView dispatch method.
        Check HTTP request methods.
        Return HTTP status 405 when request is not allowed.
        Return HTTP status 502 Bad Gateway in case connection to Elasticsearch fails.
        """

        allowed_methods = ("GET", "POST")

        # Reject disallowed requst methods
        if request.method not in allowed_methods:
            return HttpResponseNotAllowed(allowed_methods)

        # Reject POST unless request URL contains "_search" in certain place in url
        # Request URL is expected to be of form: /portalapi/<comma separated list of index names>/_search
        if request.method == "POST":
            if not re.search(r'.*\/portalapi\/[,a-zA-Z0-9]*\/_search', request.path):
                return HttpResponseNotAllowed(allowed_methods)

        # Forward request to Elasticsearch
        try:
            return super(ElasticsearchProxyView, self).dispatch(request, *args, **kwargs)
        except:
            print('Error: Cannot connect to Elasticsearch at ' + settings.ELASTICSEARCH_HOST)
            return HttpResponse(status=HTTPStatus.BAD_GATEWAY.value)

    # The Content-Type that will be added to the response in case the upstream server doesn’t send it
    default_content_type = 'application/json'

    # The max number of attempts for a request.
    retries = None

    # The URL of the proxied server.
    upstream = settings.ELASTICSEARCH_HOST


def ping(request):
    """
    Responds to request with status 200 OK.
    Used in unit test to simulate successfull response from Elasticsearch.
    """
    return HttpResponse(status=HTTPStatus.OK.value)