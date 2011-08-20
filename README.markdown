A Port of TextMate's ERB support for Sublime Text 2 (still in progress - see Coming Soon section)

Usage
=====
  Clone the repository and symlink file to Sublime's User Directory

  OS X Example
  ```
  ln -s ~/your_cloned_repo_directory/erb_block.py ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/User/erb_block.py
  ```

  Open your User Keybinding File and add the following keybinding

  { "keys": ["ctrl+shift+."], "command": "erb" }

Sample
----------
<img src="https://github.com/eddorre/SublimeERB/blob/master/erb.gif" />

Coming Soon
-----------
Adding Support for Toggling ERB styles <%= %>, <%# %>, <%= -%>, <% %>, <% -%> when there is a selection.

Copyright
---------

**SublimeERB** is Copyright (c) 2011 [Carlos Rodriguez](http://eddorre.com), released under the MIT License.