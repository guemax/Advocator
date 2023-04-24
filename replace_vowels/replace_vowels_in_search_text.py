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
from .update_vowels import update_vowels
from .. import settings


def replace_vowels_in_search_text(search_text: str) -> str:
    lower_short_vowels = settings.read('short_vowels')
    lower_long_vowels = settings.read('long_vowels')

    short_vowel_command_symbol = settings.read('short_vowel_command_symbol')
    long_vowel_command_symbol = settings.read('long_vowel_command_symbol')

    search_text = update_vowels(search_text, lower_long_vowels, long_vowel_command_symbol)
    search_text = update_vowels(search_text, lower_short_vowels, short_vowel_command_symbol)

    return search_text
