import json

# Flask stuff
from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio
from .. import global_questions_directory

from erik.dsmtw import DeSlimsteMens

game = DeSlimsteMens()

namespace = ""

@socketio.on('connect', namespace=namespace)
def io_connect():
	print("Client connected")