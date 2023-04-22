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
from anki.notes import Note

from .replace_long_vowels import update_long_vowels
from .utils import is_latin_model, note_has_been_updated


def replace_vowels(_changed: bool, note: Note, _current_field_idx: int) -> bool:
    if not is_latin_model(note):
        return False

    for name, value in note.items():
        updated_value = update_long_vowels(value)
        if not note_has_been_updated(value, updated_value):
            return False

        note[name] = updated_value
        return True
