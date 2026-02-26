# coding=utf-8
# Copyright (C) 2018-2026 by xcentaurix
# License: GNU General Public License v3.0 (see LICENSE file for details)


import Screens.Standby
from .Debug import logger
from .Version import VERSION
from . import Standby
from .ConfigInit import ConfigInit


def Plugins(**__):
    logger.info("  +++ Version: %s starts...", VERSION)
    ConfigInit()
    Screens.Standby.Standby = Standby.Standby
    Screens.Standby.TryQuitMainloop = Standby.TryQuitMainloop
    descriptors = []
    return descriptors
