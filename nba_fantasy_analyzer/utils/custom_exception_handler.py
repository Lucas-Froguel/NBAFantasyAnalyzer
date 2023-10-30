from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from nba_fantasy_analyzer.mixins.exceptions import ExceptionSerializer


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    if not response:
        try:
            data = {"message": exc.message}
            if "details" in vars(exc):
                data["details"] = exc.details
            serializer = ExceptionSerializer(data=data)
            serializer.is_valid()
            response = Response(serializer.data, status=exc.status)
        except Exception:
            response = Response(
                {"message": str(exc)}, status=status.HTTP_400_BAD_REQUEST
            )
    else:
        response.data["details"] = str(exc)

    return response
