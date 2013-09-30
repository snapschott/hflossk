import os

from flask import Blueprint, abort
from flask.ext.mako import MakoTemplates, render_template

homework = Blueprint('homework', __name__, template_folder='templates')
lectures = Blueprint('lectures', __name__, template_folder='templates')

@homework.route('/', defaults={'page': 'index'})
@homework.route('/<page>')
def display_homework(page):
    if page == 'index':
        hws = os.listdir(os.path.join(os.path.split(__file__)[0], '..',
                                      'static', 'hw'))
        hws.extend(os.listdir(os.path.join(os.path.split(__file__)[0],
                                           '..', 'templates', 'hw')))
        hws = [hw for hw in sorted(hws) if not hw == "index.mak"]

    return render_template('hw/{}.mak'.format(page), name='mako', hws=hws)

@lectures.route('/', defaults={'page': 'index'})
@lectures.route('/<page>')
def display_lecture(page):
    if page == 'index':
        lecture_notes = os.listdir(os.path.join(os.path.split(__file__)[0],
                                                '..', 'templates',
                                                'lectures'))
        lecture_notes = [note for note in sorted(lecture_notes)
                         if not note == "index.mak"]
    return render_template('lectures/{}.mak'.format(page), name='mako',
                           lectures=lecture_notes)