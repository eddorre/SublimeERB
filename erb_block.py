import sublime, sublime_plugin
import re

ERB_BLOCKS = ['<%=  %>', '<%=  -%>', '<%#  %>', '<%  %>', '<%  -%>']
ERB_REGEX = '<%(=?|-?|#?)\s{2}(-?)%>'

class ErbCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    if len(self.view.sel()) != 1:
      return

    region = self.view.sel()[0]
    if region.empty():
      if self.toggle_erb_block():
        self.replace_erb_block(edit)
      else:
        self.insert_erb_block(edit, ERB_BLOCKS[0])
    else:
      currentWord = self.view.substr(region)
      self.view.replace(edit, region, "<%%= %s  %%>" % currentWord)

  def toggle_erb_block(self):
    last_command = self.view.command_history(0)[0]
    if last_command == 'erb':
      return True
    else: return False

  def get_next_erb_block(self, selection):
    current_index = ERB_BLOCKS.index(selection.strip())
    if current_index == len(ERB_BLOCKS) - 1:
      return ERB_BLOCKS[0]
    else:
      return ERB_BLOCKS[current_index + 1]

  def insert_erb_block(self, edit, erb_block):
    region = self.view.sel()[0]

    left_most_character_region = sublime.Region(region.begin() - 1, region.begin())
    left_most_character = self.view.substr(left_most_character_region)
    right_most_character_region = sublime.Region(region.begin(), region.end() + 1)
    right_most_character = self.view.substr(right_most_character_region)

    if re.match('\s', left_most_character):
      prefix = ""
    else:
      prefix = " "

    if re.match('\s', right_most_character):
      suffix = ""
    else:
      suffix = " "

    self.view.insert(edit, region.begin(), prefix + erb_block + suffix)

    self.view.sel().clear()
    if len(erb_block) > 6:
      offset = 4 - len(suffix)
    else:
      offset = 3 - len(suffix)
    self.view.sel().add(sublime.Region(region.begin() + len(prefix) + offset + len(suffix)))

  def replace_erb_block(self, edit):
    region = self.view.sel()[0]
    new_region = sublime.Region(region.begin() - 4, region.end() + 4)
    selection = self.view.substr(new_region)

    next_erb_block = self.get_next_erb_block(selection)

    line = self.view.line(region)
    if re.match('<%(=?|-?|#?)\s{2}(-?)%>', self.view.substr(line).strip()):
      prefix = ""
      suffix = ""
    else:
      prefix = " "
      suffix = " "

    self.view.replace(edit, self.view.word(region.a), prefix + next_erb_block + suffix)
    self.view.sel().clear()

    if ERB_BLOCKS.index(next_erb_block) == 3:
      self.view.sel().add(sublime.Region(region.begin() - 1))
    elif ERB_BLOCKS.index(next_erb_block) == 0:
      self.view.sel().add(sublime.Region(region.begin() + 1))
    else:
      self.view.sel().add(sublime.Region(region.begin()))