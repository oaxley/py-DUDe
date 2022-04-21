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
# @brief	pyDUDe team/user endpoint

#----- Imports
from __future__ import annotations
from typing import Any, Dict, List, Iterator, Optional

from pyDUDe import (
    Client, exceptions,
)

from pyDUDe.config import (
    MAX_SEARCH_LIMIT, DEFAULT_SEARCH_LIMIT
)


#----- Types
T_User = Dict[str, Any]


#----- Functions
@Client.endpoint
def createTeamUser(client: Client, *, team_id: int, name: str, email: str) -> int:
    """Create a new User and associate it with this team

    Args:
        client  : the Client instance
        team_id : ID of the team
        name    : name of the user
        email   : email for this user

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        The ID of the new users
    """
    url = client._url("teams", path=f"{team_id}/users")
    body = {
        'name': name,
        'email': email
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
def getTeamUsers(client: Client, *, team_id: int, limit = DEFAULT_SEARCH_LIMIT) -> Iterator[T_User]:
    """Retrieve all the Users that belongs to a team

    Args:
        client  : the Client instance
        team_id : ID of the team
        limit   : limit the number of records for the query

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        An iterator to a Users object
    """
    url = client._url("teams", path=f"{team_id}/users")
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
def deleteTeamUsers(client: Client, *, team_id: int) -> bool:
    """Delete all the users that belongs to a team

    Args:
        client  : the Client instance
        team_id : ID of the team

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        True if all the objects have been deleted
    """
    url = client._url('teams', path=f"{team_id}/users")

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
