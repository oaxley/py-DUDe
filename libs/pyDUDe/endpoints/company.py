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
from urllib import response

import requests

from pyDUDe import (
    Client, exceptions,
)

from pyDUDe.config import (
    MAX_SEARCH_LIMIT, DEFAULT_SEARCH_LIMIT
)


#----- Functions
@Client.endpoint
def createCompany(client: Client, *, name: str) -> int:
    """Create a new company

    Args:
        client: the Client instance
        name: the name of the new company to create

    Raises:
        BadRequest, InternalServerError

    Returns:
        The Id of the new company
    """
    # URL & body for the request
    url = client.url('companies')
    body = {
        'name': name
    }

    try:
        response = requests.post(url, json=body, headers=client.headers(), verify=client.verify(), cert=client.cert())
        data = response.json()

    except Exception as e:
        raise exceptions.ConnectionError(e)

    if response.status_code == 201:
        return int(data['id'])

    # raise the proper exception depending on the status code
    exception = client.exception(response.status_code)
    raise exception(data['error']['message'])

@Client.endpoint
def getAllCompanies(client: Client, *, limit = DEFAULT_SEARCH_LIMIT) -> Iterator[Dict[str, Any]]:
    """Retrieve all the companies

    Args:
        client: the Client instance
        offset: the current offset for the search
        limit: limit the number of records

    Raises:
        ConnectionError, BadRequest, InternalServerError

    Returns:
        An iterator to a Company object
    """
    offset = 1
    url = client.url('companies')

    if limit > MAX_SEARCH_LIMIT:
        limit = MAX_SEARCH_LIMIT

    while True:
        # prepare the parameters
        params = {
            'offset': offset,
            'limit': limit
        }

        try:
            response = requests.get(url, params=params, headers=client.headers(), verify=client.verify(), cert=client.cert())
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
            exception = client.exception(response.status_code)
            raise exception(data['error']['message'])

