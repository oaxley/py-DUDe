# pyDUDe - Functions index

This symbol 🔒 indicates that accessing these functions necessitate that the configuration item *x_api_token* should be set.

---

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

---

## **[Unit](./unit.md) 🔒**

> _createUnit(*, company_id: int, name: str) -> int_  
> Create a new unit

> _getAllUnits(*, limit = DEFAULT_SEARCH_LIMIT) -> Iterator[T_Unit]_  
> Get all the units

> _deleteAllUnits() -> bool_  
> Delete all the units and their children

> _getSingleUnit(*, unit_id: int) -> T_Unit_  
> Retrieve details for a specific unit

> _updateSingleUnit(*, unit_id: int, name: Optional[str] = None) -> bool_  
> Update details for a specific unit

> _deleteSingleUnit(*, unit_id: int) -> bool_  
> Delete a specific unit

> _createUnitTeam(*, unit_id: int, name: str) -> int_  
> Create a new team and associate it with this unit

> _getUnitTeams(*, unit_id: int, limit = DEFAULT_SEARCH_LIMIT) -> Iterator[T_Team]_  
> Retrieve all the teams that belongs to a unit

---

