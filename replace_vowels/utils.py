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
from anki.decks import DeckId
from aqt import mw

from .. import settings


def dict_to_uppercase(dictionary: dict) -> dict:
    """Transform keys and values of dictionary to be uppercase."""
    return dict((key.upper(), value.upper()) for key, value in dictionary.items())


def note_has_been_updated(original_value: str, updated_value: str) -> bool:
    return updated_value != original_value


def is_latin_note(note: Note) -> bool:
    latin_note_types = settings.read('latin_note_types')
    current_note_type = note.note_type()['name'].lower()  # type: ignore  # The note type is never going to be None

    return any([latin_note_type in current_note_type for latin_note_type in latin_note_types])


def is_latin_deck(_: Note) -> bool:
    global changed_deck_name
    latin_deck_names = settings.read('latin_deck_names')

    default_deck_id = mw.col.decks.get_current_id()  # type: ignore  # As this
    # add-on will only be run inside Anki, addonManager will never be None
    default_deck_name = mw.col.decks.name(default_deck_id)  # type: ignore  # As this
    # add-on will only be run inside Anki, addonManager will never be None
    current_deck_name = changed_deck_name if changed_deck_name else default_deck_name

    return any([latin_deck_name in current_deck_name for latin_deck_name in latin_deck_names])


def set_new_deck_name(new_deck_id: int) -> None:
    global changed_deck_name
    changed_deck_name = mw.col.decks.name(DeckId(new_deck_id))  # type: ignore  # As this
    # add-on will only be run inside Anki, addonManager will never be None


changed_deck_name = ""
