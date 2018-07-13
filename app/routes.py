from flask import render_template, flash
from app import app
from app.forms import QueryForm


@app.route('/')
@app.route('/index')
def index():
    form = QueryForm()
    if form.validate_on_submit():
        flash('Query required'.format(
            form.query.data
        ))
    return render_template('index.html', title='Home', form=form)
