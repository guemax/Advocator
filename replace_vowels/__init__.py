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
from re import sub

from .utils import upper_dict

lower_long_vowels = {'a': u'ā', 'e': u'ē', 'i': u'ī', 'o': u'ō', 'u': u'ū', 'y': u'ȳ'}
upper_long_vowels = upper_dict(lower_long_vowels)

character_for_long_vowel = "_"


def update_long_vowels(word: str) -> str:
    word = __replace_vowel_with_long_vowel(lower_long_vowels, word)
    word = __replace_vowel_with_long_vowel(upper_long_vowels, word)

    return word


def __replace_vowel_with_long_vowel(long_vowels: dict, word: str) -> str:
    for vowel, long_vowel in long_vowels.items():
        word = sub(f'{vowel}{character_for_long_vowel}', long_vowel, word)

    return word
