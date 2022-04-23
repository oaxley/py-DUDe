# Team / Software functions

## _createTeamSoftware(*, team_id: int, name: str) -> int_

### **Create a new Software and associate it with this team**

    Args:
        team_id : ID of the team
        name    : name of the software

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        The ID of the new software


## _getTeamSoftware(*, team_id: int, limit = DEFAULT_SEARCH_LIMIT) -> Iterator[T_Software]_

### **Retrieve all the Software that belongs to a team**

    Args:
        team_id : ID of the team
        limit   : limit the number of records for the query

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        An iterator to a Software object


## _deleteTeamSoftware(*, team_id: int) -> bool_

### **Delete all the software that belongs to a team**

    Args:
        team_id : ID of the team

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        True if all the objects have been deleted

