import sublime, sublime_plugin
import re

ERB_BLOCKS = ['<%=  %>', '<%  %>', '<%=  -%>', '<%#  %>', '<%  -%>']
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
      self.view.replace(edit, region, "<%%= %s %%>" % currentWord)

  def toggle_erb_block(self):
    current_cursor = self.view.sel()[0].begin()
    erb_exists = self.view.find(ERB_REGEX, self.view.sel()[0].begin() - 4)

    if (erb_exists) and (erb_exists.contains(current_cursor)):
      return True
    else:
      return False

  def get_next_erb_block(self, selection):
    current_index = ERB_BLOCKS.index(selection.strip())
    if current_index == len(ERB_BLOCKS) - 1:
      return ERB_BLOCKS[0]
    else:
      return ERB_BLOCKS[current_index + 1]

  def insert_erb_block(self, edit, erb_block):
    region = self.view.sel()[0]

    self.view.insert(edit, region.begin(), erb_block)

    self.view.sel().clear()
    if len(erb_block) > 6 and erb_block != ERB_BLOCKS[-1]:
      offset = 4
    else:
      offset = 3

    self.view.sel().add(sublime.Region(region.begin() + offset))

  def replace_erb_block(self, edit):
    region = self.view.find(ERB_REGEX, self.view.sel()[0].begin() - 4)
    word = self.view.substr(region)

    next_erb_block = self.get_next_erb_block(word)

    if re.match(ERB_REGEX, word):
      self.view.erase(edit, region)
      self.insert_erb_block(edit, next_erb_block)