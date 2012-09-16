A Port of TextMate's ERB support for Sublime Text 2 (still in progress - see Coming Soon section)

Usage
=====

### Installation ###

  Suggest Installing [Sublime Package Control](http://wbond.net/sublime_packages/package_control)

  Then you can install "ERB Insert and Toggle Commands"

### Manual Installation ###

  Clone the repository and symlink file to Sublime's User Directory

  OS X Example

```
  git clone git@github.com:eddorre/SublimeERB.git ~/.sublime_erb

  ln -fs ~/.sublime_erb/erb_block.py ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/User
```

  Linux Example

```
  git clone git@github.com:eddorre/SublimeERB.git ~/.sublime_erb

  ln -fs ~/.sublime_erb/erb_block.py ~/.config/sublime-text-2/Packages/User
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
  git pull
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
