import logging
import uuid
from http import HTTPStatus

from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR

from apps.common.response.error_response import ErrorResponse

logger = logging.getLogger(__name__)


def global_exception_handler(exc, context):
    error_id = uuid.uuid4().__str__()
    logger.exception("Error [error_id=%s] [msg=%s]", error_id, exc)
    if isinstance(exc, ObjectDoesNotExist):
        return Response(status=HTTP_404_NOT_FOUND,
                        data=ErrorResponse(HTTPStatus.NOT_FOUND.phrase, exc.__str__(), error_id).__dict__)
    elif isinstance(exc, ValidationError):
        return Response(status=HTTP_400_BAD_REQUEST,
                        data=ErrorResponse(HTTPStatus.BAD_REQUEST.phrase, exc.detail, error_id).__dict__)
    else:
        return Response(status=HTTP_500_INTERNAL_SERVER_ERROR,
                        data=ErrorResponse(HTTP_500_INTERNAL_SERVER_ERROR, exc.__str__(), error_id).__dict__)
