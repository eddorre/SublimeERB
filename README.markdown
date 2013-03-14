A Port of TextMate's ERB support for Sublime Text 2 (still in progress - see Coming Soon section)

Usage
=====

### Installation ###

  I suggest Installing [Sublime Package Control](http://wbond.net/sublime_packages/package_control)

 Then you can install "ERB Insert and Toggle Commands"

#### Sublime Text 3 Beta Install ####

Make sure to follow the [updated instructions](http://wbond.net/sublime_packages/package_control/installation#ST3) for installing package control. Even with the package being installed via package control, you still need to modify you keybinding file as per the instructions below. The manual installation listed below still works for Sublime Text 3.


### Manual Installation ###

  Clone the repository and symlink file to Sublime's User Directory

  OS X Example

```
  git clone git@github.com:eddorre/SublimeERB.git ~/.sublime_erb

ln -fs ~/.sublime_erb/ ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/SublimeERB

```

  Linux Example

```
  git clone git@github.com:eddorre/SublimeERB.git ~/.sublime_erb

  ln -fs ~/.sublime_erb/ ~/.config/sublime-text-2/Packages/SublimeERB
```

  Open your User Keybinding File and add the following keybinding to activate the toggle command in all file types

```json
  [
    { "keys": ["ctrl+shift+."], "command": "erb" }
  ]
```

  or only in the most common ERB contexts

```json
  [
    { "keys": ["ctrl+shift+."], "command": "erb", "context":
      [
        { "key": "selector", "operator": "equal", "operand": "text.html.ruby, text.haml, source.yaml, source.css, source.scss, source.js, source.coffee" }
      ]
    }
  ]
```

### Update To Latest Version ###

```
  cd ~/.sublime_erb
  git pull --rebase
```

Sample
----------
<img src="https://github.com/eddorre/SublimeERB/raw/master/erb.gif" />

Coming Soon
-----------
Adding Support for Toggling ERB styles <%= %>, <%# %>, <%= -%>, <% %>, <% -%> when there is a selection.

Copyright
---------

**SublimeERB** is Copyright (c) 2011 [Carlos Rodriguez](http://eddorre.com), released under the MIT License.