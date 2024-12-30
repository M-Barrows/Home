from flask import Flask, render_template, url_for, send_from_directory
from flask_flatpages import FlatPages, pygments_style_defs

from markdown import markdown

from pygments.formatters import HtmlFormatter
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.logging import LoggingInstrumentor

from opentelemetry import trace

from feedgen.feed import FeedGenerator

import logging
from datetime import datetime, timedelta, timezone

logger = logging.getLogger(__name__)
app = Flask(__name__)
app.config.from_pyfile('config.py')
FlaskInstrumentor().instrument_app(app)
LoggingInstrumentor().instrument(set_logging_format=True)

tracer = trace.get_tracer(__name__)
pages = FlatPages(app)
tags = set(t for p in pages if (p['tags'] is not None and p['hidden'] is False) for t in p['tags'])

formatter = HtmlFormatter(style='default')
with open('static/pygments.css', 'w') as f:
    f.write(formatter.get_style_defs('.codehilite'))

fg = FeedGenerator()
fg.id('https://codecoffee.org/blog')
fg.title('Code and Coffee - Blog')
fg.author({'name': 'Code and Coffee', 'email': 'blog-info@codecoffee.org'})
fg.link(href='https://codecoffee.org/blog',rel='alternate')
fg.logo('https://codecoffee.org/static/favicon.png')
fg.subtitle('A place to share my findings with the \{hello\} world!')
fg.link(href='https://codecoffee.org/feeds',rel='self')
fg.language('en')
for post in pages:
    fe = fg.add_entry()
    fe.title(post.meta.get('title'))
    fe.id(f"https://codecoffee.org/{post.path}")
    fe.link(href=f"https://codecoffee.org/{post.path}", rel='alternate')
    fe.summary(post.meta.get('excerpt'))
    fe.content(post.html, type='html')
    dt_str = datetime.strptime(post.meta.get('date'),'%Y-%m-%d').replace(tzinfo=timezone(timedelta(hours=-5)))
    fe.pubDate(dt_str)
    fe.updated(dt_str)
fg.atom_file('./static/feed.xml')
@app.route('/')
def index():
    return render_template('index.html', pages=pages, tags=tags, page={'path':'home'})

@app.route('/blog')
def blog_home():
    return render_template('blog_home.html',pages=pages, tags=tags, page={'path':'blog'})

@app.route('/blog/tag-search/<string:tag>')
def tag_search(tag):
    return render_template('tag_search.html',pages=pages, tag=tag, tags=tags, page={'path':f'tags/{tag.lower()}'})

@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', pages=pages, page=page, tags=tags)

@app.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('tango'), 200, {'Content-Type': 'text/css'}

@app.route('/feed')
def feeds():
    return send_from_directory(directory='static',path='feed.xml')

if __name__ == '__main__':
    app.run()
