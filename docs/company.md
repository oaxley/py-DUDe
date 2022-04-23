# Company functions


## _createCompany(*, name: str) -> int_

### **Create a new company**

    Args:
        name    : the name of the new company to create

    Raises:
        BadRequest, InternalServerError

    Returns:
        The Id of the new company


## _getAllCompanies(*, limit = DEFAULT_SEARCH_LIMIT) -> Iterator[T_Company]_

### **Retrieve all the companies**

    Args:
        limit   : limit the number of records

    Raises:
        ConnectionError, BadRequest, InternalServerError

    Returns:
        An iterator to a Company object



## _deleteAllCompanies() -> bool_

### **Delete all the companies and their children**

    Args:
        client: the Client instance

    Raises:
        ConnectionError, InternalServerError

    Returns:
        True if all the companies have been deleted



## _getSingleCompany(*, company_id: int) -> T_Company_

### **Retrieve details for a specific company**

    Args:
        company_id  : ID of the company

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        The detail for the company


## _updateSingleCompany(*, name: str, company_id: int) -> bool_

### **Update details for a specific company**

    Args:
        name        : the new name for this company
        company_id  : ID of the company

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        True if the record has been updated


## _deleteSingleCompany(*, company_id: int) -> bool_

### **Delete a single company**

    Args:
        company_id  : ID of the company

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        True if the company has been deleted


## _createCompanyUnit(*, company_id: int, name: str) -> int_

### **Create a new unit and associate it with this company**

    Args
        company_id  : ID of the company
        name        : name of the unit

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        The ID of the new Unit


## _getCompanyUnits(*, company_id: int, limit = DEFAULT_SEARCH_LIMIT) -> Iterator[T_Unit]_

### **Retrieve all the units that belongs to a company**

    Args:
        company_id  : the ID of the company for the search
        limit       : limit the number of records

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        An iterator to a Unit object


## _deleteCompanyUnits(*, company_id: int) -> bool_

### **Delete all the units that belongs to a company**

    Args:
        company_id  : the ID of the company for the search

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        True if all the objects have been deleted
