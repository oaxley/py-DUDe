# User functions

## _createUser(*, team_id: int, name: str, email: str) -> int_

### **Create a new user**

    Args:
        team_id : the ID of the team to associate this user with
        name    : the name of the new user to create
        email   : the email associated with this user

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        The Id of the new user

## _getAllUsers(*, limit = DEFAULT_SEARCH_LIMIT) -> Iterator[T_User]_

### **Retrieve all users**

    Args:
        limit   : limit the number of records

    Raises:
        ConnectionError, BadRequest, InternalServerError

    Returns:
        An iterator to a User object


## _deleteAllUsers() -> bool_

### **Delete all users and their children**

    Raises:
        ConnectionError, InternalServerError

    Returns:
        True if all the users have been deleted


## _getSingleUser(*, user_id: int) -> T_User_

### **Retrieve details for a specific user**

    Args:
        user_id : ID of the user

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        The details for the unit


## _updateSingleUser(*, user_id: int, name: Optional[str] = None, email: Optional[str] = None, team_id: Optional[int] = None) -> bool_

### **Update details for a specific user**

    Args:
        user_id : ID of the user
        name    : the new name for this user
        email   : the new email for this user
        team_id : the new team ID for this user

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        True if the user has been updated


## _deleteSingleUser(*, user_id: int) -> bool_

### **Delete a specific user**

    Args:
        user_id : ID of the user

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        True if the user has been deleted

