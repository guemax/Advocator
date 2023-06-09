# Advocator: Extended latin support for Anki

> Latin: advocator, advocatoris *m* = assistent, backer

*Advocator* is an add-on providing extended latin support for Anki 2.x. It is 
based on the *[Latin Support](https://ankiweb.net/shared/info/1548612994)* 
add-on, created by Péter Dimitrov.

> **Important notice**:
> 
> Advocator is now finally available as an official add-on for Anki. 
> You can download it from https://ankiweb.net/shared/info/956356384. Please follow the instructions on that site for installing the add-on.
> 
> *Thanks!*

## Features

### Already Implemented

 - Write latin characters with ease. (Long vowels like `ā, ē, ī, ō, ū, ȳ` 
   and short vowels like `ă, ĕ, ĭ, ŏ, ŭ, y̆` as well as their capitalized 
   versions are supported.)
 - Allow easy searching for words containing long or short vowels. (A query 
   for `armare` will also return `armāre` as a search result, for example.)

### Dropped

 - Replace vowels while writing (not only when closing the editor or the field looses focus).
   *If you need a similar functionality, please have a look at the [Editor Live Preview addon](https://ankiweb.net/shared/info/1960039667) on AnkiWeb.*

## Contributing

### Reporting a bug or requesting a feature

Please use the following links to:

 - [Report a bug](https://github.com/guemax/Advocator/issues/new?assignees=&labels=bug&projects=&template=bug_report.md&title=)
 - [Request a feature](https://github.com/guemax/Advocator/issues/new?assignees=&labels=enhancement&projects=&template=feature_request.md&title=)

### Downloading the source code

First, you need to find your add-ons directory. Go to the menu item 
*Tools > Add-ons* in the main window of Anki. Click on the *View Files* button, 
and a folder will pop up. You may need to go up one level. The name of the 
folder has to be `addons21/`. Open a new terminal window in this folder.

Clone this repo either with:

```shell
git clone https://github.com/guemax/Advocator.git
# or
gh repo clone guemax/Advocator
```

Now start Anki (again) and go to *Tools > Add-ons*. You should now see an add-on 
called *Advocator*. Great, you did it! *Advocator* is now up and running.

### Writing code

You might want to have a look at the official 
[Writing Anki Add-ons](https://addon-docs.ankiweb.net/intro.html) guidelines.
