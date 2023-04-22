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
from re import sub

from .utils import dict_to_uppercase
from .. import settings


def update_short_vowels(word: str) -> str:
    lower_short_vowels = settings.read('short_vowels')
    upper_short_vowels = dict_to_uppercase(lower_short_vowels)

    word = __replace_vowel_with_short_vowel(lower_short_vowels, word)
    word = __replace_vowel_with_short_vowel(upper_short_vowels, word)

    return word


def __replace_vowel_with_short_vowel(short_vowels: dict, word: str) -> str:
    short_vowel_command_symbol = settings.read('short_vowel_command_symbol')

    for VOWEL, SHORT_VOWEL in short_vowels.items():
        word = sub(f'{VOWEL}{re.escape(short_vowel_command_symbol)}', SHORT_VOWEL, word)

    return word
