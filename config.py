import os
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.tables import TableExtension
from markdown.extensions.toc import TocExtension
from markdown.extensions.sane_lists import SaneListExtension

FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'pages'
SECRET_KEY = os.urandom(24)
FLATPAGES_MARKDOWN_EXTENSIONS = [
    FencedCodeExtension(), 
    CodeHiliteExtension(linenums=False, guess_lang=False),
    TableExtension(),
    TocExtension(anchorlink=True,title="In This Article",title_class="is-size-3"),
    SaneListExtension()]
