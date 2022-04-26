# pyDUDe - Functions index

A function that has the symbol 🔒 next to it, is an administrative function that's require the *x_api_token* to be set in the configuration.

## **[Company](./company.md) 🔒**

These functions help you manage the company data

> _createCompany(*, name: str) -> int_  
> Create a new company

> _getAllCompanies(*, limit = DEFAULT_SEARCH_LIMIT) -> Iterator[T_Company]_  
> Retrieve all the companies

> _deleteAllCompanies() -> bool_  
> Delete all the companies and their children

> _getSingleCompany(*, company_id: int) -> T_Company_  
> Retrieve details for a specific company

> _updateSingleCompany(*, name: str, company_id: int) -> bool_  
> Update details for a specific company

> _deleteSingleCompany(*, company_id: int) -> bool_  
> Delete a single company

> _createCompanyUnit(*, company_id: int, name: str) -> int_  
> Create a new unit and associate it with this company

> _getCompanyUnits(*, company_id: int, limit = DEFAULT_SEARCH_LIMIT) -> Iterator[T_Unit]_  
> Retrieve all the units that belongs to a company

> _deleteCompanyUnits(*, company_id: int) -> bool_  
> Delete all the units that belongs to a company

