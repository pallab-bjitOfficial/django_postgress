from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from .response_messages import ResponseMessage


def custom_exception_handler(exc, context):

    response = exception_handler(exc, context)

    if response is not None:
        response.data['isSuccess'] = False
        response.data['message'] = response.data.get(
            'detail', ResponseMessage.AN_ERROR_OCCURRED)
        response.data['data'] = {}
        response.data.pop('detail', None)
    else:
        response = Response({
            'isSuccess': False,
            'message': ResponseMessage.INTERNAL_SERVER_ERROR,
            'data': {}
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return response
