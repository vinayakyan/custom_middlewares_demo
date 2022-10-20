from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings


class MaintainanceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.META.get("PATH_INFO", "")
        if settings.MAINTAINANCE_MODE and path != reverse("maintainance"):
            response = redirect(reverse("maintainance"))
            return response
        response = self.get_response(request)
        return response
    