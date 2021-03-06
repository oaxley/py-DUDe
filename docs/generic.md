# Generic functions


### **Return the current API version**
_version() -> Optional[str]_

    Raises:
        ConnectionError, InternalServerError

    Returns:
        The API version string




### **Authenticate an application**
_authenticate(*, appname: str, apikey: str) -> Optional[str]_

    Args:
        appname: the application name
        apikey: the application API-KEY

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        The JSON Web Token




### **Validate a user for a specific right**
_validate(*, email: str, right: str, token: str) -> bool_

    Args:
        email: the user's email
        right: the right for which the user should be tested
        token: the JWT as returned by the auth endpoint

    Raises:
        ConnectionError, BadRequest, Unauthenticated,
        NotFound, InternalServerError

    Returns:
        True if the user is authorized, False otherwise
