#  Copyright 2025 European Union
#  Author: Bulgheroni Antonio (antonio.bulgheroni@ec.europa.eu)
#  SPDX-License-Identifier: EUPL-1.2
"""
Defines the hook specification decorator bound the MAFw library.
"""

import pluggy

from mafw.db.std_tables import StandardTable
from mafw.processor import Processor
from mafw.ui.abstract_user_interface import UserInterfaceBase

mafw_hookspec = pluggy.HookspecMarker('mafw')


@mafw_hookspec
def register_processors() -> list[Processor]:
    """Register multiple processor classes"""
    return []  # pragma: no cover


@mafw_hookspec
def register_user_interfaces() -> list[UserInterfaceBase]:
    """Register multiple user interfaces"""
    return []  # pragma: no cover


@mafw_hookspec
def register_standard_tables() -> list[StandardTable]:
    """Register standard tables"""
    return []  # pragma: no cover
