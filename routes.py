from flask import render_template
from app import app

import forms

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html', page_title='Home Page', main_title='To Do List')

@app.route('/about')
def about():
    form = forms.AddTaskForm()
    return render_template('about.html', page_title='About Page', main_title='To Do List', task_form=form)