# Software functions


### **Create a new software**
_createSoftware(*, team_id: int, name: str) -> int_

    Args:
        team_id : the ID of the team to associate this software with
        name    : the name of the new software to create

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        The Id of the new software





### **Retrieve all the software**
_getAllSoftware(*, limit = DEFAULT_SEARCH_LIMIT) -> Iterator[T_Software]_

    Args:
        limit   : limit the number of records

    Raises:
        ConnectionError, BadRequest, InternalServerError

    Returns:
        An iterator to a Software object



### **Delete all the software and their children**
_deleteAllSoftware() -> bool_

    Raises:
        ConnectionError, InternalServerError

    Returns:
        True if all the software have been deleted



### **Retrieve details for a specific software**
_getSingleSoftware(*, software_id: int) -> T_Software_

    Args:
        software_id : ID of the software

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        The details for the unit



### **Update details for a specific software**
_updateSingleSoftware(*, software_id: int, name: Optional[str] = None, team_id: Optional[int] = None) -> bool_

    Args:
        software_id : ID of the software
        name        : the new name for this software
        team_id     : the new team ID for this software

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        True if the software has been updated



### **Delete a specific software**
_deleteSingleSoftware(*, software_id: int) -> bool_

    Args:
        software_id : ID of the software

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        True if the software has been deleted
