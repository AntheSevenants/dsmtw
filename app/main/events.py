import json

# Flask stuff
from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio
from .. import global_questions_directory

from erik.dsmtw import DeSlimsteMens

game = DeSlimsteMens(["Bart", "Danira", "Liesbet"])
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