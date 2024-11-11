from django.http import JsonResponse

def url_404(request, sterings=None):
    response_data = {
        "error": "not found 404",
    }
    return JsonResponse(response_data, status=404)
