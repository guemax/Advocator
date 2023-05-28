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
from anki import hooks_gen

from .modify_search_text import modify_search_text
from .replace_vowels.utils import set_new_deck_name
from .replace_vowels import \
    replace_vowels_in_note, \
    replace_vowels_in_note_without_returning_bool


gui_hooks.browser_will_search.append(modify_search_text)
gui_hooks.editor_did_unfocus_field.append(replace_vowels_in_note)
hooks_gen.note_will_flush.append(replace_vowels_in_note_without_returning_bool)

gui_hooks.add_cards_did_change_deck.append(set_new_deck_name)
