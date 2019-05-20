from django.http import HttpResponse
from django.conf import settings

def build_info(request):
    """
    Return build information.
    """
    return HttpResponse(settings.BUILD_INFO)