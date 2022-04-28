# Company functions


### **Create a new company**
_createCompany(*, name: str) -> int_


    Args:
        name    : the name of the new company to create

    Raises:
        BadRequest, InternalServerError

    Returns:
        The Id of the new company



### **Retrieve all the companies**
_getAllCompanies(*, limit = DEFAULT_SEARCH_LIMIT) -> Iterator[T_Company]_

    Args:
        limit   : limit the number of records

    Raises:
        ConnectionError, BadRequest, InternalServerError

    Returns:
        An iterator to a Company object




### **Delete all the companies and their children**
_deleteAllCompanies() -> bool_

    Raises:
        ConnectionError, InternalServerError

    Returns:
        True if all the companies have been deleted




### **Retrieve details for a specific company**
_getSingleCompany(*, company_id: int) -> T_Company_

    Args:
        company_id  : ID of the company

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        The detail for the company



### **Update details for a specific company**
_updateSingleCompany(*, name: str, company_id: int) -> bool_

    Args:
        name        : the new name for this company
        company_id  : ID of the company

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        True if the record has been updated



### **Delete a single company**
_deleteSingleCompany(*, company_id: int) -> bool_

    Args:
        company_id  : ID of the company

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        True if the company has been deleted



### **Create a new unit and associate it with this company**
_createCompanyUnit(*, company_id: int, name: str) -> int_

    Args
        company_id  : ID of the company
        name        : name of the unit

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        The ID of the new Unit



### **Retrieve all the units that belongs to a company**
_getCompanyUnits(*, company_id: int, limit = DEFAULT_SEARCH_LIMIT) -> Iterator[T_Unit]_

    Args:
        company_id  : the ID of the company for the search
        limit       : limit the number of records

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        An iterator to a Unit object



### **Delete all the units that belongs to a company**
_deleteCompanyUnits(*, company_id: int) -> bool_

    Args:
        company_id  : the ID of the company for the search

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        True if all the objects have been deleted
