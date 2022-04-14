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
# @brief	pyDUDe team endpoint

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
T_Team = Dict[str, Any]


#----- Functions

#
# All teams
#

@Client.endpoint
def createTeam(client: Client, *, unit_id: int, name: str) -> int:
    """Create a new team and associate it with the unit

    Args:
        client  : the Client instance
        unit_id : the ID of the unit to associate this team with
        name    : the name of the new team to create

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        The Id of the new team
    """
    # URL & body for the request
    url = client._url('teams')
    body = {
        'name': name,
        'unit_id': unit_id
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
def getAllTeams(client: Client, *, limit = DEFAULT_SEARCH_LIMIT) -> Iterator[T_Team]:
    """Retrieve all the teams

    Args:
        client  : the Client instance
        limit   : limit the number of records

    Raises:
        ConnectionError, BadRequest, InternalServerError

    Returns:
        An iterator to a Team object
    """
    url = client._url('teams')
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
            for item in data['teams']:
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
def deleteAllTeams(client: Client) -> bool:
    """Delete all the teams and their children

    Args:
        client: the Client instance

    Raises:
        ConnectionError, InternalServerError

    Returns:
        True if all the teams have been deleted
    """
    try:
        response = client._delete(client._url('teams'))

    except Exception as e:
        raise exceptions.ConnectionError(e)

    if response.status_code == 204:
        return True

    # raise the proper exception depending on the status code
    exception = client._exception(response.status_code)
    data = response.json()
    raise exception(data['error']['message'])


#
# Specific Team
#

@Client.endpoint
def getSingleTeam(client: Client, *, team_id: int) -> T_Team:
    """Retrieve details for a specific team

    Args:
        client  : the Client instance
        team_id : ID of the team

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        The details for the team
    """
    url = client._url('teams', path=f"{team_id}")

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
def updateSingleTeam(client: Client, *, team_id: int, name: Optional[str] = None, unit_id: Optional[int] = None) -> bool:
    """Update details for a specific team

    Args:
        client  : the Client instance
        team_id : ID of the team
        name    : the new name for this team
        unit_id : the new company ID for this unit

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        True if the team has been updated
    """
    url = client._url('teams', path=f"{team_id}")
    body = {}

    if name:
        body['name'] = name

    if unit_id:
        body['unit_id'] = unit_id

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
def deleteSingleTeam(client: Client, *, team_id: int) -> bool:
    """Delete a specific team

    Args:
        client  : the Client instance
        team_id : ID of the team

    Raises:
        ConnectionError, NotFound, InternalServerError

    Returns:
        True if the team has been deleted
    """
    url = client._url('teams', path=f"{team_id}")

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
