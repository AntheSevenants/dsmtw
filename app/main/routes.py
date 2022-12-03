import os
import random

from flask import session, redirect, url_for, render_template, request, send_from_directory
from . import main

from .. import global_questions_directory

@main.route('/')
@main.route('/overview')
def overview(callback=None):
	return render_template('overview.html')