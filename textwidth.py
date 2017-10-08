# -*- encoding: utf-8 -*-

import sublime
import sublime_plugin
import re

from .breakline import breakline

class TextWidthReplace(sublime_plugin.TextCommand):

    def run(self, edit, region, text):
        self.view.replace(edit, sublime.Region(*region), text)

class TextWidth(sublime_plugin.ViewEventListener):

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
            newtext = breakline(v.substr(lineregion), self.textwidth)
            if newtext is None:
                return 
            self.editing = True
            v.run_command('text_width_replace', {
                'region': [lineregion.a, lineregion.b],
                'text': newtext
            })
            self.editing = False
