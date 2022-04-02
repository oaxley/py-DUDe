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
# @brief	Exception for HTTP errors 4xx


#----- Classes
class BadRequest(Exception):
    """Exception raised for HTTP status 400"""

class Unauthenticated(Exception):
    """Exception raised for HTTP status 401"""

class Forbidden(Exception):
    """Exception raised for HTTP status 403"""

class NotFound(Exception):
    """Exception raised for HTTP status 404"""
