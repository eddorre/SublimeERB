A Port of TextMate's ERB support for Sublime Text 2

## Installation

### Sublime Package Control

I suggest using [Sublime Package Control](http://wbond.net/sublime_packages/package_control). Once you have Sublime Package control installed, you can install "ERB Insert and Toggle Commands" in a few easy steps.

Press `CTRL + SHIFT + P` on Windows and Linux and `CMD + SHIFT + P` on a Mac to bring up Sublime's Command Palette, then type `install package` to bring up Package Control's package selector. It should be the first selection. Type "ERB Insert and Toggle Commands," which, again, should be the first selection, and then hit enter. You should now have the proper package installed, but you will still need to [add a keybinding to use it.](#add-keybinding)

#### Sublime Text 3 Beta Install

Make sure to follow the [updated instructions](http://wbond.net/sublime_packages/package_control/installation#ST3) for installing package control. Even with the package being installed via package control, you still need to modify you keybinding file as per the instructions below. The manual installation listed below still works for Sublime Text 3.


### Manual Installation

Clone the repository and symlink file to Sublime's User Directory:

#### OS X

```
git clone git@github.com:eddorre/SublimeERB.git ~/.sublime_erb

ln -fs ~/.sublime_erb/ ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/SublimeERB

```

#### Linux

```
git clone git@github.com:eddorre/SublimeERB.git ~/.sublime_erb

ln -fs ~/.sublime_erb/ ~/.config/sublime-text-2/Packages/SublimeERB
```

## Usage

### Add Keybinding

Open your User Keybinding File and add the following keybinding to activate the toggle command in all file types:

```json
  [
    { "keys": ["ctrl+shift+."], "command": "erb" }
  ]
```

...or only in the most common ERB contexts:

```json
  [
    { "keys": ["ctrl+shift+."], "command": "erb", "context":
      [
        { "key": "selector", "operator": "equal", "operand": "text.html.ruby, text.haml, source.yaml, source.css, source.scss, source.js, source.coffee" }
      ]
    }
  ]
```

Now you can use `ctrl+shift+.` to create and toggle between ERB tags. NOTE: On a Mac use the command key for the ctrl key.

## Update To Latest Version

```
  cd ~/.sublime_erb
  git pull --rebase
```

Sample
----------
<img src="https://github.com/eddorre/SublimeERB/raw/master/erb.gif" />

Copyright
---------

**SublimeERB** is Copyright (c) 2011 [Carlos Rodriguez](http://eddorre.com), released under the MIT License.
