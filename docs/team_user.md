# Team / User functions


### **Create a new User and associate it with this team**
_createTeamUser(*, team_id: int, name: str, email: str) -> int_

    Args:
        team_id : ID of the team
        name    : name of the user
        email   : email for this user

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        The ID of the new users



### **Retrieve all the Users that belongs to a team**
_getTeamUsers(*, team_id: int, limit = DEFAULT_SEARCH_LIMIT) -> Iterator[T_User]_

    Args:
        team_id : ID of the team
        limit   : limit the number of records for the query

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        An iterator to a Users object



### **Delete all the users that belongs to a team**
_deleteTeamUsers(*, team_id: int) -> bool_

    Args:
        team_id : ID of the team

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        True if all the objects have been deleted

