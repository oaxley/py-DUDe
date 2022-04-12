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
# @brief	pyDUDe software endpoint

#----- Imports
from __future__ import annotations
from typing import Any, Dict, List, Optional, Iterator

from pyDUDe import (
    Client, exceptions
)

from pyDUDe.config import (
    MAX_SEARCH_LIMIT, DEFAULT_SEARCH_LIMIT
)


#----- Types
T_Software = Dict[str, Any]


#----- Functions

#
# All software
#

@Client.endpoint
def createSoftware(client: Client, *, team_id: int, name: str) -> int:
    """Create a new software

    Args:
        client  : the Client instance
        team_id : the ID of the team to associate this software with
        name    : the name of the new software to create

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        The Id of the new software
    """
    # URL & body for the request
    url = client._url('software')
    body = {
        'name': name,
        'team_id': team_id
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
def getAllSoftware(client: Client, *, limit = DEFAULT_SEARCH_LIMIT) -> Iterator[T_Software]:
    """Retrieve all the software

    Args:
        client  : the Client instance
        limit   : limit the number of records

    Raises:
        ConnectionError, BadRequest, InternalServerError

    Returns:
        An iterator to a Software object
    """
    url = client._url('software')
    offset = 1

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
            for item in data['software']:
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
def deleteAllSoftware(client: Client) -> bool:
    """Delete all the software and their children

    Args:
        client: the Client instance

    Raises:
        ConnectionError, InternalServerError

    Returns:
        True if all the software have been deleted
    """
    try:
        response = client._delete(client._url('software'))

    except Exception as e:
        raise exceptions.ConnectionError(e)

    if response.status_code == 204:
        return True

    # raise the proper exception depending on the status code
    exception = client._exception(response.status_code)
    data = response.json()
    raise exception(data['error']['message'])


#
# Specific software
#

@Client.endpoint
def getSingleSoftware(client: Client, *, software_id: int) -> T_Software:
    """Retrieve details for a specific software

    Args:
        client      : the Client instance
        software_id : ID of the software

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        The details for the unit
    """
    url = client._url('software', path=f"{software_id}")

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
def updateSingleSoftware(client: Client, *, software_id: int, name: Optional[str] = None,
                      team_id: Optional[int] = None) -> bool:
    """Update details for a specific software

    Args:
        client      : the Client instance
        software_id : ID of the software
        name        : the new name for this software
        team_id     : the new team ID for this software

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        True if the software has been updated
    """
    url = client._url('software', path=f"{software_id}")
    body = {}

    if name:
        body['name'] = name

    if team_id:
        body['team_id'] = team_id

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
def deleteSingleSoftware(client: Client, *, software_id: int) -> bool:
    """Delete a specific software

    Args:
        client  : the Client instance
        software_id : ID of the software

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        True if the software has been deleted
    """
    url = client._url('software', path=f"{software_id}")

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
