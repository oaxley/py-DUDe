from .generic import (
    ConnectionError, UnknownError
)

from .http_4xx import (
    BadRequest,
    Unauthenticated,
    Forbidden,
    NotFound
)

from .http_5xx import InternalServerError
