from rest_framework import serializers


class ExceptionSerializer(serializers.Serializer):
    message = serializers.CharField()
    details = serializers.CharField(required=False)


class ExceptionMixin(Exception):
    _message: str
    status: int
    details: str

    @property
    def message(self):
        return self._message.format(**vars(self))
