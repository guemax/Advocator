# Documentation for the Advocator configuration file

## Editable values

You are free to customize these settings for changing how advocator behaves.

 - **latin_model_names**: Advocator will look for these strings in the model 
   name you are currently using for writing your words. This add-on will only 
   replace vowels when the model name for this word contains one of these 
   strings. Defaults are `latin` and `latein` (which is German for *latin*).
 - **long_vowel_command_symbol**: When Advocator finds a vowel 
   (`a, e, i, o, u or y`) in your current note with this character exactly after
   it, the add-on will replace it with the corresponding long vowel 
   (`ā, ē, ī, ō, ū or ȳ`). The default is an underscore `_`.

## Fixed values

Although you are not prevented from editing these values, it might result in a
crash or unwanted behaviour of this add-on.

 - **long_vowels**: A dictionary of the original vowels and their corresponding
   long vowels.