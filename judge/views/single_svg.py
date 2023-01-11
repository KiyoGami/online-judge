import os
from django.http import HttpResponse
from django.conf import settings


def view(request, tex, hash):
    root = settings.TEXOID_CACHE_ROOT if tex == 'texoid' else settings.MATHOID_CACHE_ROOT
    svg_path = os.path.join(root, hash, 'svg')
    svg_data = open(svg_path, 'r').read()
    return HttpResponse(svg_data, content_type='image/svg+xml')
