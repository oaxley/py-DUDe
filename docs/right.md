# Rights functions

## _createRight(*, team_id: int, name: str) -> int_

### **Create a new right**

    Args:
        team_id : the ID of the team to associate this right with
        name    : the name of the new right to create

    Raises:
        BadRequest, BadRequest, NotFound, InternalServerError

    Returns:
        The Id of the new right


## _getAllRights(*, limit = DEFAULT_SEARCH_LIMIT) -> Iterator[T_Right]_

### **Retrieve all rights**

    Args:
        limit   : limit the number of records

    Raises:
        ConnectionError, BadRequest, InternalServerError

    Returns:
        An iterator to a Right object



## _deleteAllRights() -> bool_

### **Delete all rights and their children**

    Raises:
        ConnectionError, InternalServerError

    Returns:
        True if all the rights have been deleted


## _getSingleRight(*, right_id: int) -> T_Right_

### **Retrieve details for a specific right**

    Args:
        right_id : ID of the right

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        The details for the unit


## _updateSingleRight(*, right_id: int, name: Optional[str] = None) -> bool_

### **Update details for a specific right**

    Args:
        right_id : ID of the right
        name    : the new name for this right

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        True if the right has been updated


## _deleteSingleRight(*, right_id: int) -> bool_

### **Delete a specific right**

    Args:
        right_id : ID of the right

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        True if the right has been deleted
