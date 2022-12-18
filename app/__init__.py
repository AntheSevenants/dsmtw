from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()
global_questions_directory = None
global_player_names = None

def create_app(questions_directory, player_names, debug=False):
	global global_questions_directory # it's bad but at least I know it's bad
	global global_player_names

	"""Create an application."""
	app = Flask(__name__)
	app.debug = debug
	app.config['SECRET_KEY'] = 'miep'
	global_questions_directory = questions_directory
	global_player_names = player_names

	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint, url_prefix='')

	socketio.init_app(app)
	return app