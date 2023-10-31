

class ExceptionMixin(Exception):
    _message: str
    status: int
    details: str

    @property
    def message(self):
        return self._message.format(**vars(self))
