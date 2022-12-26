import json

# Flask stuff
from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio

from flask import current_app

namespace = ""

@socketio.on('connect', namespace=namespace)
def io_connect():
	print("Client connected")
	broadcast_state()
	
def broadcast_state():
	game = current_app.config["game"]

	socketio.emit("state", game.as_dict())

def broadcast_video(video_filename):
	socketio.emit("video", video_filename)

@socketio.on('start_game', namespace=namespace)
def io_start_game():
	game = current_app.config["game"]

	game.start_game()
	broadcast_state()

@socketio.on('advance', namespace=namespace)
def io_advance():
	game = current_app.config["game"]
	
	game.advance()
	broadcast_state()

@socketio.on('advance_round', namespace=namespace)
def io_advance_round():
	game = current_app.config["game"]
	
	game.advance_round()
	broadcast_state()

@socketio.on('advance_subround', namespace=namespace)
def io_advance_subround():
	game = current_app.config["game"]
	
	game.advance_subround()
	broadcast_state()

@socketio.on('release_advance', namespace=namespace)
def io_release_advance():
	game = current_app.config["game"]
	
	to_release = game.release_advance()

	if to_release == "video":
		broadcast_video(game.current_question["video"])

	broadcast_state()

@socketio.on('answer_correct', namespace=namespace)
def io_answer_correct(answer_value):
	game = current_app.config["game"]
	
	print("Received answer:", answer_value)
	points_awarded = game.answer_correct(answer_value)
	socketio.emit("points_awarded", points_awarded)
	broadcast_state()

@socketio.on('answer_pass', namespace=namespace)
def io_answer_pass():
	game = current_app.config["game"]
	
	print("Received answer pass")
	game.answer_pass()
	broadcast_state()

@socketio.on('clock_start', namespace=namespace)
def io_clock_start():
	game = current_app.config["game"]
	
	socketio.emit("clock_start")
	game.clock_start()
	broadcast_state()

@socketio.on('clock_stop', namespace=namespace)
def io_clock_stop():
	game = current_app.config["game"]
	socketio.emit("clock_stop")
	game.clock_stop()
	broadcast_state()

@socketio.on('clock_toggle', namespace=namespace)
def io_clock_toggle():
	game = current_app.config["game"]
	
	if not game.timer_running:
		io_clock_start()
	else:
		io_clock_stop()

@socketio.on('open_deur_choose', namespace=namespace)
def io_open_deur_choose(questioneer_index):
	game = current_app.config["game"]
	
	print("Received Open deur choice:", questioneer_index)
	video_filename = game.open_deur_choose(questioneer_index)

	broadcast_state()

	if video_filename:
		broadcast_video(video_filename)