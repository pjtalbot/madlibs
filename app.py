from flask import Flask, render_template, request

from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

debug = DebugToolbarExtension(app)

@app.route('/')
def give_prompts():

    prompts = story.prompts
    return render_template("prompts.html", prompts=prompts)

@app.route('/madlib')
def show_story():

    madlib = story.generate(request.args)

    return render_template("madlib.html", madlib=madlib)