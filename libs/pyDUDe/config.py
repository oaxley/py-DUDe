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
# @brief	The config object for the DUDe python library

#----- Imports
from __future__ import annotations
from typing import Any, Optional

import pathlib

from attrs import define
from dotenv import dotenv_values


#----- Class
@define(kw_only=True)
class DUDeConfig:
    """This class encapsulates the whole configuration for the library."""

    # only keyword is supported for the initialization
    x_api_token: str = ''           # the API token for admin endpoints

    scheme: str = 'https'           # scheme for API queries
    hostname: str = ''              # API server hostname
    port: int = 5000                # API server port

    certfile: str = ''              # client certificate for SSL
    keyfile: str = ''               # key certificate for SSL
    root_ca: str = ''               # root_ca certificate to validate server SSL cert.


    def readFile(self, filename: str = '.env') -> bool:
        """Read the configuration from a .env file"""
        # if file does not exist, end there
        if not pathlib.Path(filename).exists():
            return False

        # read the file
        envcfg = dotenv_values(filename)

        # set the configuration variables
        self.x_api_token = envcfg.get('X-API-TOKEN', '')
        self.scheme = envcfg.get('SCHEME', 'https')
        self.hostname = envcfg.get('HOSTNAME', '')
        self.port = int(envcfg.get('PORT', '5000'))
        self.certfile = envcfg.get('CERTFILE', '')
        self.keyfile = envcfg.get('KEYFILE', '')
        self.root_ca = envcfg.get('ROOT_CA', '')

        return True
