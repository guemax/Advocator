"""Copyright (C) 2023 guemax

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU Affero General Public License as published by the Free
Software Foundation, version 3.
This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along
with this program. If not, see <https://www.gnu.org/licenses/>

This add-on is based on the "Latin Support" add-on, created by Péter Dimitrov
back in 2018, which is again based on the similar "Esperanto Support" add-on by
Peter Carroll.
"""
from aqt import gui_hooks
from anki.notes import Note

from .replace_vowels import update_long_vowels

latin_model_names = ['latin', 'latein']


def on_focus_lost(changed: bool, note: Note, current_field_idx: int) -> bool:
    if not __is_latin_model(note):
        return False

    for (name, value) in note.items():
        updated_value = update_long_vowels(value)
        if value != updated_value:
            note[name] = updated_value
            changed = True
    return changed


def __is_latin_model(note: Note) -> bool:
    model_name_of_note = note.model()['name'].lower()
    return any([latin_model_name in model_name_of_note for latin_model_name in latin_model_names])


gui_hooks.editor_did_unfocus_field.append(on_focus_lost)
