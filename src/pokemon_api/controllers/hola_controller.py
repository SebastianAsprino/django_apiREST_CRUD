from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def api_hola(request):
    return HttpResponse("api api XD")


# from django.http import HttpResponse
# from django.views.decorators.http import require_GET

# @require_GET
# def api_hola(request):
#     return HttpResponse("api")