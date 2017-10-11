# -*- encoding: utf-8 -*-

import sublime
import sublime_plugin
import re

from .breakline import breaklines
from Default.paragraph import expand_to_paragraph

def get_indentation_chars(settings):
    if settings.get('translate_tabs_to_spaces') is True:
        return ' ' * settings.get('tab_size')
    return '\t'

class TextwidthReplace(sublime_plugin.TextCommand):

    def run(self, edit, region, text):
        self.view.replace(edit, sublime.Region(*region), text)

class TextwidthCommand(sublime_plugin.TextCommand):

    """Re arrange the selection
    or the cursor's paragraph if it's there isn't any"""

    def run(self, edit):
        v = self.view
        settings = v.settings()
        width = settings.get('textwidth')
        ic = get_indentation_chars(settings)
        for region in v.sel():
            if region.empty():
                region = expand_to_paragraph(v, region.begin())
            result = breaklines(v.substr(region).replace('\n', ' '), width,
                                ic * v.indentation_level(region.begin()))
            if result is None:
                continue
            v.run_command('textwidth_replace',
                          {'region': [region.a, region.b],
                          'text': result})


class Textwidth(sublime_plugin.ViewEventListener):

    @classmethod
    def is_applicable(self, settings):
        self.textwidth = settings.get('textwidth')
        self.indentation_chars = get_indentation_chars(settings)
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
            if not region.empty() \
                or not v.classify(region.end()) & sublime.CLASS_LINE_END:
                continue

            lineregion = v.line(region.begin())
            newtext = breaklines(v.substr(lineregion), self.textwidth,
                                 self.indentation_chars \
                                 * v.indentation_level(lineregion.begin()))
            if newtext is None:
                return
            self.editing = True
            v.run_command('textwidth_replace', {
                'region': [lineregion.a, lineregion.b],
                'text': newtext
            })
            self.editing = False
