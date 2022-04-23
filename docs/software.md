# Software functions

## _createSoftware(*, team_id: int, name: str) -> int_

### **Create a new software**

    Args:
        team_id : the ID of the team to associate this software with
        name    : the name of the new software to create

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        The Id of the new software




## _getAllSoftware(*, limit = DEFAULT_SEARCH_LIMIT) -> Iterator[T_Software]_

### **Retrieve all the software**

    Args:
        limit   : limit the number of records

    Raises:
        ConnectionError, BadRequest, InternalServerError

    Returns:
        An iterator to a Software object


## _deleteAllSoftware() -> bool_

### **Delete all the software and their children**

    Raises:
        ConnectionError, InternalServerError

    Returns:
        True if all the software have been deleted


## _getSingleSoftware(*, software_id: int) -> T_Software_

### **Retrieve details for a specific software**

    Args:
        software_id : ID of the software

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        The details for the unit


## _updateSingleSoftware(*, software_id: int, name: Optional[str] = None, team_id: Optional[int] = None) -> bool_

### **Update details for a specific software**

    Args:
        software_id : ID of the software
        name        : the new name for this software
        team_id     : the new team ID for this software

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        True if the software has been updated


## _deleteSingleSoftware(*, software_id: int) -> bool_

### **Delete a specific software**

    Args:
        software_id : ID of the software

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        True if the software has been deleted
