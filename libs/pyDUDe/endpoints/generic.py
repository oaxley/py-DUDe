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
# @brief	Generic routes

#----- Imports
from __future__ import annotations
from typing import Any, Dict, Optional

import requests

from pyDUDe import (
    Client, exceptions
)


#----- Functions
@Client.endpoint
def version(client: Client) -> Optional[str]:
    """Return the current API version

    Args:
        client: the Client instance

    Raises:
        ConnectionError, InternalServerError

    Returns:
        The API version string
    """
    url = client.url('version')

    # send the request to the server
    try:
        response = requests.get(url, verify=client.verify(), cert=client.cert())
        data = response.json()

    except Exception as e:
        raise exceptions.ConnectionError(e)

    # return the API version
    if response.status_code == 200:
        return data['version']

    # raise the proper exception depending on the status code
    exception = client.exception(response.status_code)
    raise exception(data['error']['message'])


@Client.endpoint
def authenticate(client: Client, *, appname: str, apikey: str) -> Optional[str]:
    """Authenticate an application

    Args:
        client: the Client instance
        appname: the application name
        apikey: the application API-KEY

    Raises:
        ConnectionError, BadRequest, NotFound, InternalServerError

    Returns:
        The JSON Web Token
    """
    # URL & body for the request
    url = client.url('auth')
    body = {
        "name": appname,
        "apikey": apikey
    }

    # send the request to the server
    try:
        response = requests.post(url, json=body, verify=client.verify(), cert=client.cert())
        data = response.json()
    except Exception as e:
        raise exceptions.ConnectionError(e)

    # return the token
    if response.status_code == 200:
        return data['token']

    # raise the proper exception depending on the status code
    exception = client.exception(response.status_code)
    raise exception(data['error']['message'])


@Client.endpoint
def validate(client: Client, *, email: str, right: str, token: str) -> bool:
    """Validate a user for a specific right

    Args:
        email: the user's email
        right: the right for which the user should be tested
        token: the JWT as returned by the auth endpoint

    Raises:
        ConnectionError, BadRequest, Unauthenticated,
        NotFound, InternalServerError

    Returns:
        True if the user is authorized, False otherwise
    """
    # URL & body for the request
    url = client.url("validate")
    body = {
        'email': email,
        'right': right,
        'token': token
    }

    # send the request to the server
    try:
        response = requests.post(url, json=body, verify=client.verify(), cert=client.cert())
        data = response.json()
    except Exception as e:
        raise exceptions.ConnectionError(e)

    if response.status_code == 200:
        return True
    elif response.status_code == 403:
        return False
    else:
        # raise the proper exception depending on the status code
        exception = client.exception(response.status_code)
        raise exception(data['error']['message'])
