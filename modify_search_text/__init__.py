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


def modify_search_text(context: SearchContext) -> None:
    if context.ids:
        return

    if not is_one_word(context.search):
        return

    context.search = f"nc:{context.search}"


def is_one_word(search: str) -> bool:
    return len(search.split(" ")) == 1
