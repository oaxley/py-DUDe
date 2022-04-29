# Units functions


### **Create a new unit**
_createUnit(*, company_id: int, name: str) -> int_

    Args:
        company_id  : the ID of the company to associate this unit with
        name        : the name of the new unit to create

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        The Id of the new Unit
    


### **Get all the units**
_getAllUnits(*, limit = DEFAULT_SEARCH_LIMIT) -> Iterator[T_Unit]_

    Args:
        limit       : limit the number of records

    Raises:
        ConnectionError, BadRequest, InternalServerError

    Returns:
        An iterator to a Unit object
    


### **Delete all the units and their children**
_deleteAllUnits() -> bool_

    Raises:
        ConnectionError, InternalServerError

    Returns:
        True if all the units have been deleted
    


### **Retrieve details for a specific unit**
_getSingleUnit(*, unit_id: int) -> T_Unit_

    Args:
        unit_id : ID of the unit

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        The details for the unit
    


### **Update details for a specific unit**
_updateSingleUnit(*, unit_id: int, name: Optional[str] = None) -> bool_

    Args:
        unit_id     : ID of the unit
        name        : the new name for this unit

    Raises:
        ConnectionError, badRequest, NotFound, InternalServerError

    Returns:
        True if the unit has been updated
    


### **Delete a specific unit**
_deleteSingleUnit(*, unit_id: int) -> bool_

    Args:
        unit_id : ID of the unit

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        True if the unit has been deleted
    



### **Create a new team and associate it with this unit**
_createUnitTeam(*, unit_id: int, name: str) -> int_

    Args:
        unit_id : ID of the unit
        name    : name of the team

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        The ID of the new team
    


### **Retrieve all the teams that belongs to a unit**
_getUnitTeams(*, unit_id: int, limit = DEFAULT_SEARCH_LIMIT) -> Iterator[T_Team]_

    Args:
        unit_id : ID of the unit
        limit   : limit the number of records

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        An iterator to a Team object
    


### **Delete all the teams that belongs to a unit**
_deleteUnitTeams(*, unit_id: int) -> bool_

    Args:
        unit_id : ID of the unit

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        True if all the objects have been deleted
    
