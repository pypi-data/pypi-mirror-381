from django.conf import settings
from django.http import HttpRequest


def base16_theme(request: HttpRequest):
    _ = request
    return {"BASE16_THEME": getattr(settings, "BASE16_THEME", "circus")}
