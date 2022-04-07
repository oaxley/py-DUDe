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
from typing import Any

from pyDUDe import (
    Client, exceptions,
)

from pyDUDe.config import (
    MAX_SEARCH_LIMIT, DEFAULT_SEARCH_LIMIT
)


#----- Globals


#----- Functions
@Client.endpoint
def createUnit(client: Client, *, company_id: int, name: str) -> int:
    """Create a new company

    Args:
        client: the Client instance
        company_id: the ID of the company to associate this unit with
        name: the name of the new unit to create

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
