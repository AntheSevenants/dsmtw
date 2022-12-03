from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()
global_questions_directory = None

def create_app(questions_directory, debug=False):
	global global_questions_directory # it's bad but at least I know it's bad

	"""Create an application."""
	app = Flask(__name__)
	app.debug = debug
	app.config['SECRET_KEY'] = 'miep'
	global_questions_directory = questions_directory

	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint, url_prefix='')

	socketio.init_app(app)
	return app