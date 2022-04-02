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
# @brief	The main source for the DUDe python library

#----- Imports
from __future__ import annotations
from typing import Optional

import requests

from .config import DUDeConfig
from . import exceptions


#----- Globals


#----- Functions


#----- Class
class DUDeLib:
    """Python library to interact with the DUDe API server"""

    def __init__(self, config: DUDeConfig) -> None:
        """Constructor"""
        self.config = config


    def version(self) -> Optional[str]:
        endpoint = f"{self.config.scheme}://{self.config.hostname}:{self.config.port}/version"

        try:
            response = requests.get(endpoint, verify=self.config.root_ca)
            if response.status_code != 200:
                return None
            else:
                data = response.json()
                return data['version']

        except Exception as e:
            raise exceptions.ConnectionError(e)
