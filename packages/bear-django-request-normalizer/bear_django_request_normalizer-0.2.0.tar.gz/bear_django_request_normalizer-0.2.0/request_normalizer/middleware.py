from .RequestRepository import RequestRepository


class RequestNormalizerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        RequestRepository.convert_request_params(request)

        return self.get_response(request)