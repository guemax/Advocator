# Documentation for the Advocator configuration file

## Editable values

You are free to customize these settings for changing how advocator behaves.

 - **latin_note_types**: Advocator will look for these strings in the note 
   type you are currently using for writing your words. This add-on will only 
   replace vowels when the note type for this word contains one of these 
   strings. Defaults are `latin` and `latein` (which is German for *latin*).
 - **latin_deck_names**: Advocator not only searches for `latin_note_types`, but
   also checks if the name of the deck matches a name specified in this array. 
   This way *Advocator* works in a deck no matter what note type you are 
   currently using. Defaults are `Latein Vokabeln` (German), `latin vocab` and
   `latin vocabulary`.
 - **long_vowel_command_symbol**: When Advocator finds a vowel 
   (`a, e, i, o, u or y`) in your current note with this character exactly after
   it, the add-on will replace it with the corresponding long vowel 
   (`ā, ē, ī, ō, ū or ȳ`). The default is an underscore `_`.
 - **short_vowel_command_symbol**: When Advocator finds a vowel 
   (`a, e, i, o, u or y`) in your current note with this character exactly after
   it, the add-on will replace it with the corresponding short vowel 
   (`ă, ĕ, ĭ, ŏ, ŭ or y̆`). The default is an asterisk `*`.
 - **disable_modification_of_search_text_by_addon_command**: Advocator will 
   usually append a query like `amare` with `nc:` to also match words like 
   `armāre`. This behaviour can be prevented by adding this piece of text to your
   query. Default is `disable:advocator`.

## Fixed values

Although you are not prevented from editing these values, it might result in a
crash or unwanted behaviour of this add-on.

 - **long_vowels**: A dictionary of the original vowels and their corresponding
   long vowels.
 - **short_vowels**: A dictionary of the original vowels and their corresponding
   short vowels.