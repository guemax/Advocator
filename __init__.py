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


def on_focus_lost(flag, n, fidx):
    if "latin" not in n.model()['name'].lower():
        return flag
    for (name, value) in n.items():
        updated_value = replace_with_macros(value)
        if value != updated_value:
            n[name] = updated_value
            flag = True
    return flag


def replace_with_macros(value):
    from re import sub
    tmp = sub("a`", u"ā", value)
    tmp = sub("e`", u"ē", tmp)
    tmp = sub("i`", u"ī", tmp)
    tmp = sub("o`", u"ō", tmp)
    tmp = sub("u`", u"ū", tmp)
    tmp = sub("y`", u"ȳ", tmp)
    tmp = sub("A`", u"Ā", tmp)
    tmp = sub("E`", u"Ē", tmp)
    tmp = sub("I`", u"Ī", tmp)
    tmp = sub("O`", u"Ō", tmp)
    tmp = sub("U`", u"Ū", tmp)
    tmp = sub("Y`", u"Ȳ", tmp)
    return tmp


gui_hooks.editor_did_unfocus_field.append(on_focus_lost)
