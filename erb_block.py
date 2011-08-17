import sublime, sublime_plugin
import re

ERB_BLOCKS = ['<%=  %>', '<%  %>', '<%-  -%>', '<%  -%>']

class ErbCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    if len(self.view.sel()) != 1:
      return

    region = self.view.sel()[0]
    cursor_location = region.begin()
    if region.empty():
      if self.in_erb_block():
        self.replace_erb_block(edit)
      else:
        self.insert_erb_block(edit, ERB_BLOCKS[0])
        # txt = view.substr(sublime.Region(pos, end_position))
    else:
      currentWord = self.view.substr(region)
      self.view.replace(edit, region, " <%%= %s  %%> " % currentWord)

  def in_erb_block(self):
    region = self.view.sel()[0]

    if region.begin() != 0:
      selection = self.view.substr(sublime.Region(region.begin() - 4, region.end() + 4))
      match =  re.match('<%(=?|-?)\s{2}(-?)%>', selection)
      if match:
        return True
      else:
        return False
    else:
      return False

  def last_erb_block(self):
    region = self.view.sel()[0]
    return self.view.substr(sublime.Region(region.begin() - 4, region.end() + 4))

  def get_next_erb_block(self):
    current_index = ERB_BLOCKS.index(self.last_erb_block())
    if current_index == len(ERB_BLOCKS) - 1:
      return ERB_BLOCKS[0]
    else:
      return ERB_BLOCKS[current_index + 1]

  def insert_erb_block(self, edit, erb_block):
    region = self.view.sel()[0]
    self.view.insert(edit, region.begin(), erb_block)
    self.view.sel().clear()
    self.view.sel().add(sublime.Region(region.begin() + 4))

  def replace_erb_block(self, edit):
    region = self.view.sel()[0]
    next_erb_block = self.get_next_erb_block()
    self.view.replace(edit, self.view.word(region.a), next_erb_block)
    self.view.sel().clear()

    if ERB_BLOCKS.index(next_erb_block) == 1:
      self.view.sel().add(sublime.Region(region.begin() - 1))
    elif ERB_BLOCKS.index(next_erb_block) == len(ERB_BLOCKS) - 1:
      self.view.sel().add(sublime.Region(region.begin() - 1))
    elif ERB_BLOCKS.index(next_erb_block) == 2:
      self.view.sel().add(sublime.Region(region.begin() + 1))
    elif ERB_BLOCKS.index(next_erb_block) == 0:
      self.view.sel().add(sublime.Region(region.begin() + 1))
    else:
      self.view.sel().add(sublime.Region(region.begin()))