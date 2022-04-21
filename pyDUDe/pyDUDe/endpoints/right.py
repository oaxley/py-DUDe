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
# @brief	pyDUDe right endpoint

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
T_Right = Dict[str, Any]


#----- Functions

#
# All rights
#

@Client.endpoint
def createRight(client: Client, *, team_id: int, name: str) -> int:
    """Create a new right

    Args:
        client  : the Client instance
        team_id : the ID of the team to associate this right with
        name    : the name of the new right to create

    Raises:
        BadRequest, BadRequest, NotFound, InternalServerError

    Returns:
        The Id of the new right
    """
    # URL & body for the request
    url = client._url('rights')
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
def getAllRights(client: Client, *, limit = DEFAULT_SEARCH_LIMIT) -> Iterator[T_Right]:
    """Retrieve all the rights

    Args:
        client  : the Client instance
        limit   : limit the number of records

    Raises:
        ConnectionError, BadRequest, InternalServerError

    Returns:
        An iterator to a Right object
    """
    url = client._url('rights')
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
            for item in data['rights']:
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
def deleteAllRights(client: Client) -> bool:
    """Delete all the rights and their children

    Args:
        client: the Client instance

    Raises:
        ConnectionError, InternalServerError

    Returns:
        True if all the rights have been deleted
    """
    try:
        response = client._delete(client._url('rights'))

    except Exception as e:
        raise exceptions.ConnectionError(e)

    if response.status_code == 204:
        return True

    # raise the proper exception depending on the status code
    exception = client._exception(response.status_code)
    data = response.json()
    raise exception(data['error']['message'])


#
# Specific right
#

@Client.endpoint
def getSingleRight(client: Client, *, right_id: int) -> T_Right:
    """Retrieve details for a specific right

    Args:
        client  : the Client instance
        right_id : ID of the right

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        The details for the unit
    """
    url = client._url('rights', path=f"{right_id}")

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
def updateSingleRight(client: Client, *, right_id: int, name: Optional[str] = None) -> bool:
    """Update details for a specific right

    Args:
        client  : the Client instance
        right_id : ID of the right
        name    : the new name for this right

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        True if the right has been updated
    """
    url = client._url('rights', path=f"{right_id}")
    body = {}

    if name:
        body['name'] = name

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
def deleteSingleRight(client: Client, *, right_id: int) -> bool:
    """Delete a specific right

    Args:
        client  : the Client instance
        right_id : ID of the right

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        True if the right has been deleted
    """
    url = client._url('rights', path=f"{right_id}")

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
