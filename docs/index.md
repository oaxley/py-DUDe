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

## **[Team](./team.md) 🔒**

> _createTeam(*, unit_id: int, name: str) -> int_  
> Create a new team and associate it with the unit

> _getAllTeams(*, limit = DEFAULT_SEARCH_LIMIT) -> Iterator[T_Team]_  
> Retrieve all the teams

> _deleteAllTeams(client: Client) -> bool_  
> Delete all the teams and their children

> _getSingleTeam(*, team_id: int) -> T_Team_  
> Retrieve details for a specific team

> _updateSingleTeam(*, team_id: int, name: Optional[str] = None, unit_id: Optional[int] = None) -> bool_  
> Update details for a specific team

> _deleteSingleTeam(*, team_id: int) -> bool_  
> Delete a specific team

---

## **[Team/User](./team_user.md) 🔒**

> _createTeamUser(*, team_id: int, name: str, email: str) -> int_  
> Create a new User and associate it with this team

> _getTeamUsers(*, team_id: int, limit = DEFAULT_SEARCH_LIMIT) -> Iterator[T_User]_  
> Retrieve all the Users that belongs to a team

> _deleteTeamUsers(*, team_id: int) -> bool_  
> Delete all the users that belongs to a team

---

## **[Team/Right](./team_right.md) 🔒**

> _createTeamRight(*, team_id: int, name: str) -> int_  
> Create a new Right and associate it with this team

> _getTeamRights(*, team_id: int, limit = DEFAULT_SEARCH_LIMIT) -> Iterator[T_Right]_  
> Retrieve all the Rights that belongs to a team

> _deleteTeamRights(*, team_id: int) -> bool_  
> Delete all the Rights that belongs to a team

---

## **[Team/Software](./team_software.md) 🔒**

> _createTeamSoftware(*, team_id: int, name: str) -> int_  
> Create a new Software and associate it with this team

> _getTeamSoftware(*, team_id: int, limit = DEFAULT_SEARCH_LIMIT) -> Iterator[T_Software]_  
> Retrieve all the Software that belongs to a team

> _deleteTeamSoftware(*, team_id: int) -> bool_  
> Delete all the software that belongs to a team

---

## **[User](./user.md) 🔒**


> _createUser(*, team_id: int, name: str, email: str) -> int_  
> Create a new user

> _getAllUsers(*, limit = DEFAULT_SEARCH_LIMIT) -> Iterator[T_User]_  
> Retrieve all users

> _deleteAllUsers() -> bool_  
> Delete all users and their children

> _getSingleUser(*, user_id: int) -> T_User_  
> Retrieve details for a specific user

> _updateSingleUser(*, user_id: int, name: Optional[str] = None, email: Optional[str] = None, team_id: Optional[int] = None) -> bool_  
> Update details for a specific user

> _deleteSingleUser(*, user_id: int) -> bool_  
> Delete a specific user

---

## **[Right](./right.md) 🔒**

> _createRight(*, team_id: int, name: str) -> int_  
> Create a new right

> _getAllRights(*, limit = DEFAULT_SEARCH_LIMIT) -> Iterator[T_Right]_  
> Retrieve all rights

> _deleteAllRights() -> bool_  
> Delete all rights and their children

> _getSingleRight(*, right_id: int) -> T_Right_  
> Retrieve details for a specific right

> _updateSingleRight(*, right_id: int, name: Optional[str] = None) -> bool_  
> Update details for a specific right

> _deleteSingleRight(*, right_id: int) -> bool_  
> Delete a specific right

---

## **[Software](./software.md) 🔒**

> _createSoftware(*, team_id: int, name: str) -> int_  
> Create a new software

> _getAllSoftware(*, limit = DEFAULT_SEARCH_LIMIT) -> Iterator[T_Software]_  
> Retrieve all the software

> _deleteAllSoftware() -> bool_  
> Delete all the software and their children

> _getSingleSoftware(*, software_id: int) -> T_Software_  
> Retrieve details for a specific software

> _updateSingleSoftware(*, software_id: int, name: Optional[str] = None, team_id: Optional[int] = None) -> bool_  
> Update details for a specific software

> _deleteSingleSoftware(*, software_id: int) -> bool_  
> Delete a specific software
