from flask import render_template, request, session, redirect, flash, url_for, abort
from app import create_app, pagination
from app.utils import url_for_other_page, extract_tags, login_required
from config import config

app = create_app(config)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', meta_title='404'), 404


@app.template_filter('formatdate')
def format_datetime_filter(input_value, format_="%a, %d %b %Y"):
    return input_value.strftime(format_)


app.jinja_env.globals['url_for_other_page'] = url_for_other_page
app.jinja_env.globals['meta_description'] = app.config['BLOG_DESCRIPTION']


app.run(host="0.0.0.0", port=5000, debug=app.config['DEBUG'])