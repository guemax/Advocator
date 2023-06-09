"""Copyright (C) 2023 guemax

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU Affero General Public License as published by the Free
Software Foundation, version 3.
This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along
with this program. If not, see <https://www.gnu.org/licenses/>
"""
from typing import Any

from aqt import mw


def read(key: str) -> Any:
    config: dict[str, Any] = mw.addonManager.getConfig(__name__)  # type: ignore  # As this
    # add-on will only be run inside Anki, addonManager will never be None
    return config[key]


def write(key: str, value: Any) -> None:
    config: dict[str, Any] = mw.addonManager.getConfig(__name__)  # type: ignore  # As this
    # add-on will only be run inside Anki, addonManager will never be None
    config[key] = value

    mw.addonManager.writeConfig(__name__, config)  # type: ignore  # As this
    # add-on will only be run inside Anki, addonManager will never be None
