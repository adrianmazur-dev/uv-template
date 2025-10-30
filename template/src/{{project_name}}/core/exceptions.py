from __future__ import annotations


class CoreException(Exception):
    pass


class ValidationError(CoreException):
    pass


class NotFoundError(CoreException):
    pass
