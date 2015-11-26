import sublime, sublime_plugin
import re

TWIG_BLOCKS = [['{{', '}}'], ['{%', '%}'], ['{#', '#}']]
TWIG_REGEX = '<%(=?|-?|#?)\s{2}(-?)%>'

# matches opening bracket that is not followed by the closing one
TWIG_OPENER_REGEX = '<%[\=\-\#]?(?!.*%>)'
# matches the closing bracket. I couldn't figure out a way to exclude preceeding
# opening bracket, since Python only support fixed-width negative lookbehind
TWIG_CLOSER_REGEX = '-?%>'

class TwigCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    if len(self.view.sel()) < 1:
      return

    # storing all new cursor positions to ensure they stay where they were before the changes
    new_selections = []

    # looping through each selection
    for region in self.view.sel():

      # searching for an opening bracket and closing bracket
      opener, closer = self.find_surrounding_blocks(region)

      if (opener is not None) and (closer is not None):
        # if brackets found - replacing them with the next ones. Result is a new cursor position.
        new_selections.append(self.replace_twig_block(edit, opener, closer, region))
      else:
        # if the brackets were't found - inserting new ones. Result is a new cursor position.
        new_selections.append(self.insert_twig_block(edit, region))

    # clearing current selections
    self.view.sel().clear()

    # looping through the modified selections and adding them
    for selection in new_selections:
      self.view.sel().add(selection)

  def find_surrounding_blocks(self, region):
    opener = None
    closer = None

    # grabbing the whole line
    containing_line = self.view.line(region)

    # one region to the left of the selection and one to the right
    left_region = sublime.Region(containing_line.begin(), region.begin())
    right_region = sublime.Region(containing_line.end(), region.end())

    # searching in the left region for an opening bracket
    found_openers = list(re.finditer(TWIG_OPENER_REGEX, self.view.substr(left_region)))
    if len(found_openers) > 0:
      # if found, creating a region for it, using the last match - the rightmost bracket found
      opener = sublime.Region(left_region.begin() + found_openers[-1].start(), left_region.begin() + found_openers[-1].end())

    # searching for a closing brcket in the right region
    found_closers = list(re.finditer(TWIG_CLOSER_REGEX, self.view.substr(right_region)))
    if len(found_closers) > 0:
      # if found, creating a new region, using the first match - the leftmost bracket found
      closer = sublime.Region(right_region.begin() + found_closers[0].start(), right_region.begin() + found_closers[0].end())

    return opener, closer

  def insert_twig_block(self, edit, region):
    # inserting the first block in the list
    default_block = TWIG_BLOCKS[0]

    # inserting in reverse order because line length might change
    self.view.insert(edit, region.end(), " %s" % default_block[1])
    inserted_before = self.view.insert(edit, region.begin(), "%s " % default_block[0])

    # returning a region, shifted by the number of inserted characters before the cursor
    return sublime.Region(region.begin() + inserted_before, region.end() + inserted_before)

  def replace_twig_block(self, edit, opener, closer, region):
    # getting the next block in the list
    next_block = self.get_next_twig_block(self.view.substr(opener), self.view.substr(closer))

    # calculating by how many characters the selection will change
    changed_before = len(next_block[0]) - len(self.view.substr(opener))

    # replacing in reverse order because line length might change
    self.view.replace(edit, closer, next_block[1])
    self.view.replace(edit, opener, next_block[0])

    # returning a region, shifted by the number of difference of characters changed
    return sublime.Region(region.begin() + changed_before, region.end() + changed_before)

  def get_next_twig_block(self, opening_bracket, closing_bracket):
    for i, block in enumerate(TWIG_BLOCKS):
      if [opening_bracket, closing_bracket] == block:
        # if outside of scope - returning the first block
        if i + 1 >= len(TWIG_BLOCKS):
          return TWIG_BLOCKS[0]
        else:
          return TWIG_BLOCKS[i + 1]

    # in case we haven't found the block in the list, returning the first one
    return TWIG_BLOCKS[0]
