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
# @brief	pyDUDe unit endpoint

#----- Imports
from __future__ import annotations
from typing import Any, Dict, List, Iterator

from pyDUDe import (
    Client, exceptions,
)

from pyDUDe.config import (
    MAX_SEARCH_LIMIT, DEFAULT_SEARCH_LIMIT
)


#----- Types
T_Unit = Dict[str, Any]



#----- Functions

#
# All units
#

@Client.endpoint
def createUnit(client: Client, *, company_id: int, name: str) -> int:
    """Create a new company

    Args:
        client      : the Client instance
        company_id  : the ID of the company to associate this unit with
        name        : the name of the new unit to create

    Raises:
        BadRequest, NotFound, InternalServerError

    Returns:
        The Id of the new company
    """
    url = client._url('units')
    body = {
        'name': name,
        'company_id': company_id
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
def getAllUnits(client: Client, *, limit = DEFAULT_SEARCH_LIMIT) -> Iterator[T_Unit]:
    """Get all the units

    Args:
        client      : the Client instance
        limit       : limit the number of records

    Raises:
        ConnectionError, BadRequest, InternalServerError

    Returns:
        An iterator to a Unit object
    """
    offset = 1
    url = client._url('units')

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
def deleteAllUnits(client: Client) -> bool:
    """Delete all the units and their children

    Args:
        client: the Client instance

    Raises:
        ConnectionError, InternalServerError

    Returns:
        True if all the units have been deleted
    """
    try:
        response = client._delete(client._url('units'))

    except Exception as e:
        raise exceptions.ConnectionError(e)

    if response.status_code == 204:
        return True

    # raise the proper exception depending on the status code
    exception = client._exception(response.status_code)
    data = response.json()
    raise exception(data['error']['message'])
