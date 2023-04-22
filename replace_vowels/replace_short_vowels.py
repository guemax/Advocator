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
    short_vowel_command_symbol = settings.read('short_vowel_command_symbol')

    return update_vowels(word, lower_short_vowels, short_vowel_command_symbol)


def update_vowels(word: str, lower_vowels: dict, vowel_command_symbol: str) -> str:
    upper_vowels = dict_to_uppercase(lower_vowels)

    word = __replace_vowel_with_corresponding_vowel(lower_vowels, word, vowel_command_symbol)
    word = __replace_vowel_with_corresponding_vowel(upper_vowels, word, vowel_command_symbol)

    return word


def __replace_vowel_with_corresponding_vowel(vowels: dict, word: str, vowel_command_symbol: str) -> str:
    for vowel, corresponding_vowel in vowels.items():
        word = sub(f'{vowel}{re.escape(vowel_command_symbol)}', corresponding_vowel, word)

    return word
