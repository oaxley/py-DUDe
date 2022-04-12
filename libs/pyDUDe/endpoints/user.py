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
# @brief	pyDUDe user endpoint

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
T_User = Dict[str, Any]


#----- Functions

#
# All users
#

@Client.endpoint
def createUser(client: Client, *, team_id: int, name: str, email: str) -> int:
    """Create a new user

    Args:
        client  : the Client instance
        team_id : the ID of the team to associate this user with
        name    : the name of the new user to create
        email   : the email associated with this user

    Raises:
        BadRequest, NotFound, InternalServerError

    Returns:
        The Id of the new user
    """
    # URL & body for the request
    url = client._url('users')
    body = {
        'name': name,
        'email': email,
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
def getAllUsers(client: Client, *, limit = DEFAULT_SEARCH_LIMIT) -> Iterator[T_User]:
    """Retrieve all the users

    Args:
        client  : the Client instance
        limit   : limit the number of records

    Raises:
        ConnectionError, BadRequest, InternalServerError

    Returns:
        An iterator to a User object
    """
    url = client._url('users')
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
            for item in data['users']:
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
def deleteAllUsers(client: Client) -> bool:
    """Delete all the users and their children

    Args:
        client: the Client instance

    Raises:
        ConnectionError, InternalServerError

    Returns:
        True if all the users have been deleted
    """
    try:
        response = client._delete(client._url('users'))

    except Exception as e:
        raise exceptions.ConnectionError(e)

    if response.status_code == 204:
        return True

    # raise the proper exception depending on the status code
    exception = client._exception(response.status_code)
    data = response.json()
    raise exception(data['error']['message'])


#
# Specific user
#

@Client.endpoint
def getSingleUser(client: Client, *, user_id: int) -> T_User:
    """Retrieve details for a specific user

    Args:
        client  : the Client instance
        user_id : ID of the user

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        The details for the unit
    """
    url = client._url('users', path=f"{user_id}")

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
def updateSingleUser(client: Client, *, user_id: int, name: Optional[str] = None,
                     email: Optional[str] = None, team_id: Optional[int] = None) -> bool:
    """Update details for a specific user

    Args:
        client  : the Client instance
        user_id : ID of the user
        name    : the new name for this user
        email   : the new email for this user
        team_id : the new team ID for this user

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        True if the user has been updated
    """
    url = client._url('users', path=f"{user_id}")
    body = {}

    if name:
        body['name'] = name

    if email:
        body['email'] = email

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
def deleteSingleUser(client: Client, *, user_id: int) -> bool:
    """Delete a specific user

    Args:
        client  : the Client instance
        user_id : ID of the user

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        True if the user has been deleted
    """
    url = client._url('users', path=f"{user_id}")

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
