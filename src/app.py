from flask import Flask, render_template
from flask_flatpages import FlatPages, pygments_style_defs
from markdown import markdown
from pygments.formatters import HtmlFormatter
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from prometheus_flask_exporter import PrometheusMetrics
from opentelemetry import trace

app = Flask(__name__)
app.config.from_pyfile('config.py')
FlaskInstrumentor().instrument_app(app)
metrics = PrometheusMetrics(app)
tracer = trace.get_tracer(__name__)
pages = FlatPages(app)
tags = set(t for p in pages if (p['tags'] is not None and p['hidden'] is False) for t in p['tags'])

formatter = HtmlFormatter(style='default')
with open('static/pygments.css', 'w') as f:
    f.write(formatter.get_style_defs('.codehilite'))

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

if __name__ == '__main__':
    app.run()
