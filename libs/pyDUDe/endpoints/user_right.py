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
# @brief	pyDUDe user-right endpoint

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
T_UserRight = Dict[str, Any]


#----- Functions

#
# All user-rights
#

@Client.endpoint
def createUserRight(client: Client, *, user_id: int, right_id: int) -> int:
    """Create a new user-right association

    Args:
        client   : the Client instance
        user_id  : the ID of the user for this association
        right_id : the ID of the right for this association

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        The Id of the new user-right association
    """
    # URL & body for the request
    url = client._url('user-rights')
    body = {
        'user_id': user_id,
        'right_id': right_id
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
def getAllUserRights(client: Client, *, limit = DEFAULT_SEARCH_LIMIT) -> Iterator[T_UserRight]:
    """Retrieve all user-right associations

    Args:
        client  : the Client instance
        limit   : limit the number of records

    Raises:
        ConnectionError, BadRequest, InternalServerError

    Returns:
        An iterator to a User object
    """
    url = client._url('user-rights')
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
            for item in data['user-rights']:
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
def deleteAllUserRights(client: Client) -> bool:
    """Delete all the user-right associations

    Args:
        client: the Client instance

    Raises:
        ConnectionError, InternalServerError

    Returns:
        True if all the user-right associations have been deleted
    """
    try:
        response = client._delete(client._url('user-rights'))

    except Exception as e:
        raise exceptions.ConnectionError(e)

    if response.status_code == 204:
        return True

    # raise the proper exception depending on the status code
    exception = client._exception(response.status_code)
    data = response.json()
    raise exception(data['error']['message'])

#
# Specific user-right
#

@Client.endpoint
def getSingleUserRight(client: Client, *, userright_id: int) -> T_UserRight:
    """Retrieve details for a specific user/right association

    Args:
        client       : the Client instance
        userright_id : ID of the user-right association

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        The details for the unit
    """
    url = client._url('user-rights', path=f"{userright_id}")

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
def updateSingleUserRight(client: Client, *, userright_id: int,
                            user_id: Optional[int] = None, right_id: Optional[int] = None) -> bool:
    """Update details for a specific user-right association

    Args:
        client       : the Client instance
        userright_id : ID of the user-right association
        user_id      : ID of the new user for this association
        right_id     : ID of the new right for this association

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        True if the user has been updated
    """
    url = client._url('user-rights', path=f"{userright_id}")
    body = {}

    if user_id:
        body['user_id'] = user_id

    if right_id:
        body['right_id'] = right_id

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
def deleteSingleUserRight(client: Client, *, userright_id: int) -> bool:
    """Delete a specific user-right association

    Args:
        client       : the Client instance
        userright_id : ID of the user-right association

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        True if the user has been deleted
    """
    url = client._url('user-rights', path=f"{userright_id}")

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

