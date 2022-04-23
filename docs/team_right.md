# Team / Right functions

## _createTeamRight(*, team_id: int, name: str) -> int_

### **Create a new Right and associate it with this team**

    Args:
        team_id : ID of the team
        name    : name of the right

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        The ID of the new rights

## _getTeamRights(*, team_id: int, limit = DEFAULT_SEARCH_LIMIT) -> Iterator[T_Right]_

### **Retrieve all the Rights that belongs to a team**

    Args:
        team_id : ID of the team
        limit   : limit the number of records for the query

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        An iterator to a Rights object


## _deleteTeamRights(*, team_id: int) -> bool_

### **Delete all the Rights that belongs to a team**

    Args:
        team_id : ID of the team

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        True if all the objects have been deleted

