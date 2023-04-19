#
# Latin Support for Anki 2.1
#
# Copyright Péter Dimitrov 2018-2020
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
#
# 2018-12-27: Initial version
# 2020-09-06: Fix crash with Anki 2.1.33
#

# Adds support for the special latin characters with macron:
# <vowel> + ''' is replaced with the same character but with a
# macron when the input field changes ("a`" -> "ā")
# Based on the similar "Esperanto Support for Anki 2.0" by
# Peter Carroll.
#
from anki.hooks import addHook


def onFocusLost(flag, n, fidx):
    from aqt import mw
    # latin model?
    if "latin" not in n.model()['name'].lower():
        return flag
    for (name, value) in n.items():
        updatedValue = replaceWithMacrons(value)
        if value != updatedValue:
            n[name] = updatedValue
            flag = True
    return flag


def replaceWithMacrons(value):
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


addHook('editFocusLost', onFocusLost)
