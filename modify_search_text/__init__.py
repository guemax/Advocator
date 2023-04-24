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
from aqt.browser import SearchContext

from .. import settings


def modify_search_text(context: SearchContext) -> None:
    if context.ids:
        return

    search_text_modification_disabled_command = settings.read('disable_modification_of_search_text_by_addon_command')
    if is_more_than_one_word(context.search) \
            or search_text_modification_disabled_by_user(context.search, search_text_modification_disabled_command):
        context.search.replace(search_text_modification_disabled_command, "")
        return

    context.search = f"nc:{context.search}"


def is_more_than_one_word(search: str) -> bool:
    return len(search.split(" ")) > 1


def search_text_modification_disabled_by_user(search: str, search_text_modification_disabled_command: str) -> bool:
    return search_text_modification_disabled_command in search
