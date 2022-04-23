# Team / User functions

## _createTeamUser(*, team_id: int, name: str, email: str) -> int_

### **Create a new User and associate it with this team**

    Args:
        team_id : ID of the team
        name    : name of the user
        email   : email for this user

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        The ID of the new users


## _getTeamUsers(*, team_id: int, limit = DEFAULT_SEARCH_LIMIT) -> Iterator[T_User]_

### **Retrieve all the Users that belongs to a team**

    Args:
        team_id : ID of the team
        limit   : limit the number of records for the query

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        An iterator to a Users object


## _deleteTeamUsers(*, team_id: int) -> bool_

### **Delete all the users that belongs to a team**

    Args:
        team_id : ID of the team

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        True if all the objects have been deleted

