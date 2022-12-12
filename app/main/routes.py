import os
import random

from flask import session, redirect, url_for, render_template, request, send_file
from . import main

from .. import global_questions_directory

@main.route('/')
@main.route('/overview')
def overview(callback=None):
	return render_template('game.html', host=True)

@main.route('/resources/<string:filename>')
def display_label_image(filename):
	if not os.path.isabs(global_questions_directory):
		path = os.path.join("..", global_questions_directory, filename)
	else:
		path = os.path.join(global_questions_directory, filename)

	return send_file(path)