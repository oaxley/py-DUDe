# -*- coding: utf-8 -*-
# vim: set ft=python
#
# This source file is subject to the Apache License 2.0
# that is bundled with this package in the file LICENSE.txt.
# It is also available through the Internet at this address:
# https://opensource.org/licenses/Apache-2.0
#
# @author	Sebastien LEGRAND
# @license	Apache License 2.0
#
# @brief	pyDUDe company endpoint

#----- Imports
from __future__ import annotations
from typing import Any, Dict, List, Optional, Iterator

from pyDUDe import (
    Client, exceptions,
)

from pyDUDe.config import (
    MAX_SEARCH_LIMIT, DEFAULT_SEARCH_LIMIT
)


#----- Types
T_Company = Dict[str, Any]
T_Unit = Dict[str, Any]


#----- Functions

#
# All companies
#

@Client.endpoint
def createCompany(client: Client, *, name: str) -> int:
    """Create a new company

    Args:
        client  : the Client instance
        name    : the name of the new company to create

    Raises:
        BadRequest, InternalServerError

    Returns:
        The Id of the new company
    """
    # URL & body for the request
    url = client._url('companies')
    body = {
        'name': name
    }

    try:
        response = client._post(url, body)
        data = response.json()

    except Exception as e:
        raise exceptions.ConnectionError(e)

    if response.status_code == 201:
        return int(data['id'])

    # raise the proper exception depending on the status code
    exception = client._exception(response.status_code)
    raise exception(data['error']['message'])


@Client.endpoint
def getAllCompanies(client: Client, *, limit = DEFAULT_SEARCH_LIMIT) -> Iterator[T_Company]:
    """Retrieve all the companies

    Args:
        client  : the Client instance
        limit   : limit the number of records

    Raises:
        ConnectionError, BadRequest, InternalServerError

    Returns:
        An iterator to a Company object
    """
    offset = 1
    url = client._url('companies')

    if limit > MAX_SEARCH_LIMIT:
        limit = MAX_SEARCH_LIMIT

    while True:
        # prepare the parameters
        params = {
            'offset': offset,
            'limit': limit
        }

        try:
            response = client._get(url, params)
            data = response.json()

        except Exception as e:
            raise exceptions.ConnectionError(e)

        if response.status_code == 200:
            for item in data['companies']:
                yield item

            if int(data['count']) < int(data['limit']):
                break
            else:
                offset += int(data['count'])

        else:
            # raise the proper exception depending on the status code
            exception = client._exception(response.status_code)
            raise exception(data['error']['message'])


@Client.endpoint
def deleteAllCompanies(client: Client) -> bool:
    """Delete all the companies and their children

    Args:
        client: the Client instance

    Raises:
        ConnectionError, InternalServerError

    Returns:
        True if all the companies have been deleted
    """
    try:
        response = client._delete(client._url('companies'))

    except Exception as e:
        raise exceptions.ConnectionError(e)

    if response.status_code == 204:
        return True

    # raise the proper exception depending on the status code
    exception = client._exception(response.status_code)
    data = response.json()
    raise exception(data['error']['message'])


#
# Specific company
#

@Client.endpoint
def getSingleCompany(client: Client, *, company_id: int) -> T_Company:
    """Retrieve details for a specific company

    Args:
        client      : the Client instance
        company_id  : ID of the company

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        The detail for the company
    """
    url = client._url('companies', path=f"{company_id}")

    try:
        response = client._get(url)
        data = response.json()

    except Exception as e:
        raise exceptions.ConnectionError(e)

    if response.status_code == 200:
        return data

    # raise the proper exception depending on the status code
    exception = client._exception(response.status_code)
    raise exception(data['error']['message'])


@Client.endpoint
def updateSingleCompany(client: Client, *, name: str, company_id: int) -> bool:
    """Update details for a specific company

    Args:
        client      : the Client instance
        name        : the new name for this company
        company_id  : ID of the company

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        True if the record has been updated
    """
    url = client._url('companies', path=f"{company_id}")
    body = {
        'name': name
    }

    try:
        response = client._put(url, body)

    except Exception as e:
        raise exceptions.ConnectionError(e)

    if response.status_code == 204:
        return True

    # raise the proper exception depending on the status code
    exception = client._exception(response.status_code)
    data = response.json()
    raise exception(data['error']['message'])


@Client.endpoint
def deleteSingleCompany(client: Client, *, company_id: int) -> bool:
    """Delete a single company

    Args:
        client      : the Client instance
        company_id  : ID of the company

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        True if the company has been deleted
    """
    url = client._url('companies', path=f"{company_id}")

    try:
        response = client._delete(url)

    except Exception as e:
        raise exceptions.ConnectionError(e)

    if response.status_code == 204:
        return True

    # raise the proper exception depending on the status code
    exception = client._exception(response.status_code)
    data = response.json()
    raise exception(data['error']['message'])


#
# Company / Units
#

@Client.endpoint
def createCompanyUnit(client: Client, *, company_id: int, name: str) -> int:
    """Create a new unit and associate it with this company

    Args
        client      : the Client instance
        company_id  : ID of the company
        name        : name of the unit

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        True if the company has been deleted
    """
    url = client._url('companies', path=f"{company_id}/units")
    body = {
        'name': name
    }

    try:
        response = client._post(url, body)
        data = response.json()

    except Exception as e:
        raise exceptions.ConnectionError(e)

    if response.status_code == 201:
        return int(data['id'])

    # raise the proper exception depending on the status code
    exception = client._exception(response.status_code)
    raise exception(data['error']['message'])


@Client.endpoint
def getCompanyUnits(client: Client, *, company_id: int, limit = DEFAULT_SEARCH_LIMIT) -> Iterator[T_Unit]:
    """Retrieve all the units that belongs to a company

    Args:
        client      : the Client instance
        company_id  : the ID of the company for the search
        limit       : limit the number of records

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        An iterator to a Unit object
    """
    offset = 1
    url = client._url('companies', path=f"{company_id}/units")

    if limit > MAX_SEARCH_LIMIT:
        limit = MAX_SEARCH_LIMIT

    while True:
        # prepare the parameters
        params = {
            'offset': offset,
            'limit': limit
        }

        try:
            response = client._get(url, params)
            data = response.json()

        except Exception as e:
            raise exceptions.ConnectionError(e)

        if response.status_code == 200:
            for item in data['units']:
                yield item

            if int(data['count']) < int(data['limit']):
                break
            else:
                offset += int(data['count'])

        else:
            # raise the proper exception depending on the status code
            exception = client._exception(response.status_code)
            raise exception(data['error']['message'])


@Client.endpoint
def deleteCompanyUnits(client: Client, *, company_id: int) -> bool:
    """Delete all the units that belongs to a company

    Args:
        client      : the Client instance
        company_id  : the ID of the company for the search

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        True if all the objects have been deleted
    """
    url = client._url('companies', path=f"{company_id}/units")

    try:
        response = client._delete(url)

    except Exception as e:
        raise exceptions.ConnectionError(e)

    if response.status_code == 204:
        return True

    # raise the proper exception depending on the status code
    exception = client._exception(response.status_code)
    data = response.json()
    raise exception(data['error']['message'])
