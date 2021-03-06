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
from typing import Any, ClassVar, Dict, Tuple, Optional

import requests

from functools import wraps

from .config import DUDeConfig
from . import exceptions


#----- Class
class Client:
    """Singleton class to access the DUDe server"""

    # only one instance of this class is available
    __instance: ClassVar[Optional[Client]] = None

    def __new__(cls: Client) -> Client:
        """Create a new instance of the class or return the current one"""
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            cls.__instance._setup()

        return cls.__instance

    def _setup(self) -> None:
        """Method called to initialize the instance after its creation"""
        # configuration
        self._config = DUDeConfig()

        # mapping HTTP error code and exceptions
        self.error_map: Dict[int, Exception] = {

            400: exceptions.BadRequest,
            401: exceptions.Unauthenticated,
            403: exceptions.Forbidden,
            404: exceptions.NotFound,
            500: exceptions.InternalServerError,

            999: exceptions.UnknownError
        }

    @property
    def config(self) -> DUDeConfig:
        """Retrieve the current DUDeConfig object"""
        return self._config

    @config.setter
    def config(self, config: DUDeConfig) -> None:
        """Set the current DUDeConfig object"""
        self._config = config

    def _exception(self, value) -> Exception:
        """Retrieve the proper exception corresponding to the HTTP error

        Args:
            value: the HTTP error

        Returns:
            An exception
        """
        return self.error_map.get(value, 999)


    def _url(self, endpoint: str, *, path: str = "") -> str:
        """Return the proper URL to connect to the specified endpoint

        Args:
            endpoint: the endpoint to connect to

        Returns:
            the complete URL to use to connect to the endpoint
        """
        value = f"{self._config.scheme}://{self._config.hostname}:{self._config.port}/{endpoint}"
        if len(path) > 0:
            value = f"{value}/{path}"

        return value

    def _verify(self) -> Optional[str]:
        """Check the SSL parameter

        Returns:
            None if we are not using SSL, the /path/to/certificate otherwise
        """
        if self._config.root_ca != '':
            return self._config.root_ca
        else:
            return None

    def _cert(self) -> Optional[Tuple[str, str]]:
        """Check if a client SSL certificate should be used

        Returns:
            A Tuple with the certificate and the key for this client, None otherwise
        """
        if (self._config.certfile != '') and (self._config.keyfile != ''):
            return (self._config.certfile, self._config.keyfile)
        else:
            return None

    def _headers(self) -> Dict[str, str]:
        """Add necessary headers

        Returns:
            A dictionary that can be used as a headers in requests
        """
        headers = {}
        if self._config.x_api_token != '':
            headers['X-API-Token'] = self._config.x_api_token

        return headers

    def _request(self, *, request: str = "", url: str = "", params: Optional[Dict[str, Any]] = None, body: Dict[str, Any] = {}) -> requests.Response:
        """Execute a request and return the data

        Args:
            request: the type of the request (POST, GET, PUT, DELETE)
            url: the URL for the request
            params: parameters for the request if any
            body: body data for the request if any
        """
        # extra arguments for requests
        kwargs = {
            'headers': self._headers(),
            'verify': self._verify(),
            'cert': self._cert()
        }

        if request == "GET":
            response = requests.get(url, params, **kwargs)

        elif request == "POST":
            response = requests.post(url, json=body, **kwargs)

        elif request == "PUT":
            response = requests.put(url, json=body, **kwargs)

        elif request == "DELETE":
            response = requests.delete(url, **kwargs)

        else:
            raise ValueError(f"Error: unknown method [{request}] called.")

        return response


    def _get(self, url: str = "", params: Optional[Dict[str, Any]] = None) -> requests.Response:
        """Execute a HTTP GET request"""
        return self._request(request="GET", url=url, params=params)

    def _post(self, url: str = "", body: Dict[str, Any] = {}) -> requests.Response:
        """Execute a HTTP POST request"""
        return self._request(request="POST", url=url, body=body)

    def _put(self, url: str = "", body: Dict[str, Any] = {}) -> requests.Response:
        """Execute a HTTP PUT request"""
        return self._request(request="PUT", url=url, body=body)

    def _delete(self, url: str = "") -> requests.Response:
        """Execute a HTTP PUT request"""
        return self._request(request="DELETE", url=url)


    @staticmethod
    def endpoint(fn):
        """Decorator to define endpoints"""
        @wraps(fn)
        def wrapper(*args, **kwargs):
            # add the client instance at the beginning of each functions
            return fn(Client(), *args, **kwargs)

        # add the function to the client namespace
        setattr(Client(), fn.__name__, wrapper)

        return wrapper
