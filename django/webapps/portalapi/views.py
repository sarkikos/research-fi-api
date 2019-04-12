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


class PublicationProxyView(ProxyView):
    """
    Handle Publications api request.

    Proxies GET request to Elasticsearch.
    All other HTTP requests are blocked and responded with status code 405 Method Not Allowed.
    """

    def dispatch(self, request, *args, **kwargs):
        """
        Extend ProxyView dispatch method.
        Check that type of HTTP request is GET.
        Return HTTP status 502 Bad Gateway in case connection to Elasticsearch fails.
        """
        if request.method != 'GET':
            # Return 405 Method Not Allowed.
            # Argument to the constructor is a list of permitted methods.
            return HttpResponseNotAllowed(['GET'])

        try:
            return super(PublicationProxyView, self).dispatch(request, *args, **kwargs)
        except:
            print('Error: Cannot connect to Elasticsearch at ' + settings.ELASTICSEARCH_HOST)
            return HttpResponse(status=HTTPStatus.BAD_GATEWAY.value)

    # The Content-Type that will be added to the response in case the upstream server doesn’t send it
    default_content_type = 'application/json'

    # The max number of attempts for a request.
    retries = None

    # The URL of the proxied server.
    upstream = settings.ELASTICSEARCH_HOST + '/publication'