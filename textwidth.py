# -*- encoding: utf-8 -*-

import sublime
import sublime_plugin
import re

from .breakline import breaklines
from Default.paragraph import expand_to_paragraph

class TextwidthReplace(sublime_plugin.TextCommand):

    def run(self, edit, region, text):
        self.view.replace(edit, sublime.Region(*region), text)

class TextwidthCommand(sublime_plugin.TextCommand):

    """Re arrange the selection
    or the cursor's paragraph if it's there isn't any"""

    def run(self, edit):
        width = self.view.settings().get('textwidth')
        for region in self.view.sel():
            if region.empty():
                region = expand_to_paragraph(self.view, region.begin())
            result = breaklines(self.view.substr(region).replace('\n', ' '), width)
            if result is None:
                continue
            self.view.run_command('text_width_replace', {'region': [region.a, region.b],
                                                         'text': result})


class Textwidth(sublime_plugin.ViewEventListener):

    @classmethod
    def is_applicable(self, settings):
        self.textwidth = settings.get('textwidth')
        self.editing = False
        return isinstance(self.textwidth, int)

    @classmethod
    def applies_to_primary_view_only(self):
        return True

    def on_modified(self):
        if self.editing:
            return
        v = self.view
        for region in v.sel():
            if not region.empty():
                continue

            lineregion = v.line(region.begin())
            newtext = breaklines(v.substr(lineregion), self.textwidth)
            if newtext is None:
                return 
            self.editing = True
            v.run_command('text_width_replace', {
                'region': [lineregion.a, lineregion.b],
                'text': newtext
            })
            self.editing = False
