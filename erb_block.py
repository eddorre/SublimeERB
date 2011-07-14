import sublime, sublime_plugin

class ErbCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    if len(self.view.sel()) != 1:
      return

    region = self.view.sel()[0]
    if region.empty():
      # Nothing is selected
      self.view.insert(edit, region.begin(), "<%= %>")
    else:
      currentWord = self.view.substr(region)
      self.view.replace(edit, region, " <%%= %s %%> " % currentWord)