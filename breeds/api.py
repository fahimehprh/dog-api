from django.http import JsonResponse

from .errors import ServiceError


class APIJSONResponse:
    def __init__(self, serializer=None, error_message=None):
        self.serializer = serializer
        self.error_message = error_message

    def response(self):
        if self.error_message:
            return JsonResponse({
                'result': 'error',
                'message': self.error_message,
            }, status=400)
        return JsonResponse({
            'result': 'success',
            'data': self.serializer.serialize(),
        }, status=200)


def api(view_func):
    def wrapper(*args, **kwargs) -> JsonResponse:
        try:
            result = view_func(*args, **kwargs)
        except ServiceError as e:
            return APIJSONResponse(error_message=str(e)).response()
        if not isinstance(result, APIJSONResponse):
            return APIJSONResponse(error_message='Unknown error occurred.').response()
        return result.response()

    return wrapper
