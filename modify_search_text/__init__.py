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
import re

from aqt.browser import SearchContext

from .. import replace_vowels
from .. import settings


def modify_search_text(context: SearchContext) -> None:
    if context.ids:
        return

    if should_not_modify_search_text(context.search):
        context.search = remove_disable_command_from_search_text_if_necessary(context.search)
        return

    # TODO: Is this really a *feature* we need to have? Isn't this already taken on by the filter `nc:'?
    context.search = replace_vowels.replace_vowels_in_search_text(context.search)
    context.search = f"nc:{context.search}"


def should_not_modify_search_text(search: str) -> bool:
    return is_more_than_one_word(search) \
        or search_text_modification_disabled_by_user(search) \
        or advanced_search_filter_has_been_applied(search)


def is_more_than_one_word(search: str) -> bool:
    return len(search.split(" ")) > 1


def advanced_search_filter_has_been_applied(search: str) -> bool:
    # Matches strings like `id:123', `nid:123', `nc:bonjour', ...
    return bool(re.search(r'\w+:\w+', search))


def search_text_modification_disabled_by_user(search: str) -> bool:
    disable_command = settings.read('disable_modification_of_search_text_by_addon_command')
    return disable_command in search


def remove_disable_command_from_search_text_if_necessary(search: str) -> str:
    disable_command = settings.read('disable_modification_of_search_text_by_addon_command')
    return search.replace(disable_command, "")
