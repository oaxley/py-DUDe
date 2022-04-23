# Units functions

## _createUnit(*, company_id: int, name: str) -> int_

### **Create a new unit**

    Args:
        company_id  : the ID of the company to associate this unit with
        name        : the name of the new unit to create

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        The Id of the new Unit
    

## _getAllUnits(*, limit = DEFAULT_SEARCH_LIMIT) -> Iterator[T_Unit]_

### **Get all the units**

    Args:
        limit       : limit the number of records

    Raises:
        ConnectionError, BadRequest, InternalServerError

    Returns:
        An iterator to a Unit object
    

## _deleteAllUnits() -> bool_

### **Delete all the units and their children**

    Raises:
        ConnectionError, InternalServerError

    Returns:
        True if all the units have been deleted
    

## _getSingleUnit(*, unit_id: int) -> T_Unit_

### **Retrieve details for a specific unit**

    Args:
        unit_id : ID of the unit

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        The details for the unit
    

## _updateSingleUnit(*, unit_id: int, name: Optional[str] = None) -> bool_

### **Update details for a specific unit**

    Args:
        unit_id     : ID of the unit
        name        : the new name for this unit

    Raises:
        ConnectionError, badRequest, NotFound, InternalServerError

    Returns:
        True if the unit has been updated
    

## _deleteSingleUnit(*, unit_id: int) -> bool_

### **Delete a specific unit**

    Args:
        unit_id : ID of the unit

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        True if the unit has been deleted
    


## _createUnitTeam(*, unit_id: int, name: str) -> int_

### **Create a new team and associate it with this unit**

    Args:
        unit_id : ID of the unit
        name    : name of the team

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        The ID of the new team
    

## _getUnitTeams(*, unit_id: int, limit = DEFAULT_SEARCH_LIMIT) -> Iterator[T_Team]_

### **Retrieve all the teams that belongs to a unit**

    Args:
        unit_id : ID of the unit
        limit   : limit the number of records

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        An iterator to a Team object
    

## _deleteUnitTeams(*, unit_id: int) -> bool_

### **Delete all the teams that belongs to a unit**

    Args:
        unit_id : ID of the unit

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        True if all the objects have been deleted
    
