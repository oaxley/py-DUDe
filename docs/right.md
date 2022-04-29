# Rights functions


### **Create a new right**
_createRight(*, team_id: int, name: str) -> int_

    Args:
        team_id : the ID of the team to associate this right with
        name    : the name of the new right to create

    Raises:
        BadRequest, BadRequest, NotFound, InternalServerError

    Returns:
        The Id of the new right



### **Retrieve all rights**
_getAllRights(*, limit = DEFAULT_SEARCH_LIMIT) -> Iterator[T_Right]_

    Args:
        limit   : limit the number of records

    Raises:
        ConnectionError, BadRequest, InternalServerError

    Returns:
        An iterator to a Right object




### **Delete all rights and their children**
_deleteAllRights() -> bool_

    Raises:
        ConnectionError, InternalServerError

    Returns:
        True if all the rights have been deleted



### **Retrieve details for a specific right**
_getSingleRight(*, right_id: int) -> T_Right_

    Args:
        right_id : ID of the right

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        The details for the unit



### **Update details for a specific right**
_updateSingleRight(*, right_id: int, name: Optional[str] = None) -> bool_

    Args:
        right_id : ID of the right
        name    : the new name for this right

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        True if the right has been updated



### **Delete a specific right**
_deleteSingleRight(*, right_id: int) -> bool_

    Args:
        right_id : ID of the right

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        True if the right has been deleted
