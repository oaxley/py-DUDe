# Team functions

### **Create a new team and associate it with the unit**
_createTeam(*, unit_id: int, name: str) -> int_

    Args:
        unit_id : the ID of the unit to associate this team with
        name    : the name of the new team to create

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        The Id of the new team

### **Retrieve all the teams**
_getAllTeams(*, limit = DEFAULT_SEARCH_LIMIT) -> Iterator[T_Team]_

    Args:
        limit   : limit the number of records

    Raises:
        ConnectionError, BadRequest, InternalServerError

    Returns:
        An iterator to a Team object

### **Delete all the teams and their children**
_deleteAllTeams(client: Client) -> bool_

    Raises:
        ConnectionError, InternalServerError

    Returns:
        True if all the teams have been deleted

### **Retrieve details for a specific team**
_getSingleTeam(*, team_id: int) -> T_Team_

    Args:
        team_id : ID of the team

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        The details for the team

### **Update details for a specific team**
_updateSingleTeam(*, team_id: int, name: Optional[str] = None, unit_id: Optional[int] = None) -> bool_

    Args:
        team_id : ID of the team
        name    : the new name for this team
        unit_id : the new unit ID for this team

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        True if the team has been updated

### **Delete a specific team**
_deleteSingleTeam(*, team_id: int) -> bool_

    Args:
        team_id : ID of the team

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        True if the team has been deleted
