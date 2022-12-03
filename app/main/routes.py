import os
import random

from flask import session, redirect, url_for, render_template, request, send_file
from . import main

from .. import global_questions_directory

@main.route('/')
@main.route('/overview')
def overview(callback=None):
	return render_template('overview.html')

@main.route('/resources/<string:round_text>/<string:filename>')
def display_label_image(round_text, filename):
	if not os.path.isabs(global_questions_directory):
		path = os.path.join("..", global_questions_directory, round_text, filename)
	else:
		path = os.path.join(global_questions_directory, round_text, filename)

	return send_file(path)