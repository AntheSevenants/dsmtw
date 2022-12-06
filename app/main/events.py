import json

# Flask stuff
from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio
from .. import global_questions_directory

from erik.dsmtw import DeSlimsteMens

game = DeSlimsteMens(["Bart", "Danira", "Liesbet"], global_questions_directory)
game.start_game() # temporary!

namespace = ""

@socketio.on('connect', namespace=namespace)
def io_connect():
	print("Client connected")
	broadcast_state()
	
def broadcast_state():
	socketio.emit("state", game.as_dict())

def broadcast_video(video_filename):
	socketio.emit("video", video_filename)

@socketio.on('advance', namespace=namespace)
def io_advance():
	game.advance()
	broadcast_state()

@socketio.on('advance_round', namespace=namespace)
def io_advance_round():
	game.advance_round()
	broadcast_state()

@socketio.on('advance_subround', namespace=namespace)
def io_advance_subround():
	game.advance_subround()
	broadcast_state()

@socketio.on('answer_correct', namespace=namespace)
def io_answer_correct(answer_value):
	print("Received answer:", answer_value)
	game.answer_correct(answer_value)
	broadcast_state()

@socketio.on('answer_pass', namespace=namespace)
def io_answer_pass():
	print("Received answer pass")
	game.answer_pass()
	broadcast_state()

@socketio.on('clock_start', namespace=namespace)
def io_clock_start():
	game.clock_start()
	broadcast_state()

@socketio.on('clock_stop', namespace=namespace)
def io_clock_stop():
	game.clock_stop()
	broadcast_state()

@socketio.on('open_deur_choose', namespace=namespace)
def io_open_deur_choose(questioneer_index):
	print("Received Open deur choice:", questioneer_index)
	video_filename = game.open_deur_choose(questioneer_index)

	broadcast_state()

	if video_filename:
		broadcast_video(video_filename)