# Team functions

## _createTeam(*, unit_id: int, name: str) -> int_
### **Create a new team and associate it with the unit**

    Args:
        unit_id : the ID of the unit to associate this team with
        name    : the name of the new team to create

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        The Id of the new team

## _getAllTeams(*, limit = DEFAULT_SEARCH_LIMIT) -> Iterator[T_Team]_
### **Retrieve all the teams**

    Args:
        limit   : limit the number of records

    Raises:
        ConnectionError, BadRequest, InternalServerError

    Returns:
        An iterator to a Team object

## _deleteAllTeams(client: Client) -> bool_
### **Delete all the teams and their children**

    Raises:
        ConnectionError, InternalServerError

    Returns:
        True if all the teams have been deleted

## _getSingleTeam(*, team_id: int) -> T_Team_
### **Retrieve details for a specific team**

    Args:
        team_id : ID of the team

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        The details for the team

## _updateSingleTeam(*, team_id: int, name: Optional[str] = None, unit_id: Optional[int] = None) -> bool_
### **Update details for a specific team**

    Args:
        team_id : ID of the team
        name    : the new name for this team
        unit_id : the new unit ID for this team

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        True if the team has been updated

## _deleteSingleTeam(*, team_id: int) -> bool_
### **Delete a specific team**

    Args:
        team_id : ID of the team

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        True if the team has been deleted
