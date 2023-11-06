import os

from django.conf import settings
from django.http import HttpResponse, HttpResponseNotFound
from django.views.static import serve


def protected_serve(request, path, document_root=None, show_indexes=False):
    if path.startswith('public/') or request.user.is_authenticated:
        if os.getenv('ENV') not in ['prod', 'prep', 'staging']:
            return serve(request, path, document_root, show_indexes)
        else:
            response = HttpResponse(status=200)
            response['Content-Type'] = ''
            response['X-Accel-Redirect'] = (settings.WEB_SERVER_MEDIA_URL + path).encode('utf-8')
            return response
    return HttpResponseNotFound()
