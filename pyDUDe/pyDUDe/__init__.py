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
# @brief	pyDUDe package init file

#----- Imports
from .core import Client
from .config import DUDeConfig

from . import exceptions
from . import endpoints


#----- Globals
__version__ = "1.0.0"
