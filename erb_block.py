import sublime, sublime_plugin
import re

ERB_BLOCKS = [['<%=', '%>'], ['<%', '%>'], ['<%-', '-%>'], ['<%=', '-%>'], ['<%#', '%>'], ['<%', '-%>']]
ERB_REGEX = '<%(=?|-?|#?)\s{2}(-?)%>'

ERB_OPENER_REGEX = '<%[\=\-\#]?(?!.*%>)'
ERB_CLOSER_REGEX = '-?%>'

class ErbCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    if len(self.view.sel()) < 1:
      return

    new_selections = []

    for region in self.view.sel():
      opener, closer = self.find_surrounding_blocks(region)

      if (opener is not None) and (closer is not None):
        new_selections.append(self.replace_erb_block(edit, opener, closer, region))
      else:
        new_selections.append(self.insert_erb_block(edit, region))

    self.view.sel().clear()
    for selection in new_selections:
      self.view.sel().add(selection)

  def find_surrounding_blocks(self, region):
    opener = None
    closer = None

    containing_line = self.view.line(region)

    left_region = sublime.Region(containing_line.begin(), region.begin())
    right_region = sublime.Region(containing_line.end(), region.end())

    found_openers = list(re.finditer(ERB_OPENER_REGEX, self.view.substr(left_region)))
    if (len(found_openers) > 0):
      opener = sublime.Region(left_region.begin() + found_openers[-1].start(), left_region.begin() + found_openers[-1].end())

    found_closers = list(re.finditer(ERB_CLOSER_REGEX, self.view.substr(right_region)))
    if (len(found_closers) > 0):
      closer = sublime.Region(right_region.begin() + found_closers[0].start(), right_region.begin() + found_closers[0].end())

    return opener, closer

  def insert_erb_block(self, edit, region):
    default_block = ERB_BLOCKS[0]

    # inserting in reverse order because line length might change
    self.view.insert(edit, region.end(), " %s" % default_block[1])
    inserted_before = self.view.insert(edit, region.begin(), "%s " % default_block[0])

    return sublime.Region(region.begin() + inserted_before, region.end() + inserted_before)

  def replace_erb_block(self, edit, opener, closer, region):
    next_block = self.get_next_erb_block(self.view.substr(opener), self.view.substr(closer))

    changed_before = len(next_block[0]) - len(self.view.substr(opener))

    # replacing in reverse order because line length might change
    self.view.replace(edit, closer, next_block[1])
    self.view.replace(edit, opener, next_block[0])

    return sublime.Region(region.begin() + changed_before, region.end() + changed_before)

  def get_next_erb_block(self, opening_bracket, closing_bracket):
    for i, block in enumerate(ERB_BLOCKS):
      if [opening_bracket, closing_bracket] == block:
        if i + 1 >= len(ERB_BLOCKS):
          return ERB_BLOCKS[0]
        else:
          return ERB_BLOCKS[i + 1]

    return ERB_BLOCKS[0]