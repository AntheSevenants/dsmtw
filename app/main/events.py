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