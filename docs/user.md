# User functions


### **Create a new user**
_createUser(*, team_id: int, name: str, email: str) -> int_

    Args:
        team_id : the ID of the team to associate this user with
        name    : the name of the new user to create
        email   : the email associated with this user

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        The Id of the new user


### **Retrieve all users**
_getAllUsers(*, limit = DEFAULT_SEARCH_LIMIT) -> Iterator[T_User]_

    Args:
        limit   : limit the number of records

    Raises:
        ConnectionError, BadRequest, InternalServerError

    Returns:
        An iterator to a User object



### **Delete all users and their children**
_deleteAllUsers() -> bool_

    Raises:
        ConnectionError, InternalServerError

    Returns:
        True if all the users have been deleted



### **Retrieve details for a specific user**
_getSingleUser(*, user_id: int) -> T_User_

    Args:
        user_id : ID of the user

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        The details for the unit



### **Update details for a specific user**
_updateSingleUser(*, user_id: int, name: Optional[str] = None, email: Optional[str] = None, team_id: Optional[int] = None) -> bool_

    Args:
        user_id : ID of the user
        name    : the new name for this user
        email   : the new email for this user
        team_id : the new team ID for this user

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        True if the user has been updated



### **Delete a specific user**
_deleteSingleUser(*, user_id: int) -> bool_

    Args:
        user_id : ID of the user

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        True if the user has been deleted

