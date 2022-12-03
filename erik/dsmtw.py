import json
import os.path

from gameshow.gameshow import Gameshow

class DeSlimsteMens(Gameshow):
	def __init__(self, players):
		rounds = [ "3-6-9", "Open deur", "Puzzel", "Galerij", "Collectief geheugen",
				   "Finale" ]

		no_players = len(players)

		super().__init__("De Slimste Mens Ter Wereld", rounds, no_players)

		self.set_active_player(0)
		self.reset_turn_history()

		for i, player in enumerate(players):
			self.players[i].name = player

	# We use the turn history to keep track of which players have already had a guess
	# in this specific subround. This allows game-crucial mechanics such as keeping track
	# of who can complement an answer first
	def reset_turn_history(self):
		self.turn_history = []

	# Add the index of the current player to the turn history
	def add_current_player_to_turn_history(self):
		self.turn_history.append(self.active_player_index)

	# Do simple turn advancement which is not based on seconds
	# Only used in 3-6-9
	# Turns will advance "simply" from 1 -> 2 -> 3 etc.
	def advance_turn_simply(self):
		if len(self.turn_history) == self.no_players:
			# Give the turn back to the first player if this turn
			self.set_active_player(self.turn_history[0])
			# Then advance the subround
			# This must be done *after* setting the active player, because
			# advancing the subround empties the turn history
			self.advance_subround()
			return

		# If we need to advance the turn, but we need to "wrap" to the first player
		if self.turn_history[-1] == self.no_players - 1:
			self.set_active_player(0)
		# We get the last player, and we add 1 to get the "next" player
		else:
			self.set_active_player(self.turn_history[-1] + 1)

	# Advance the subround, and clear the turn history
	def advance_subround(self):
		super().advance_subround()
		self.reset_turn_history()

	def answer_correct(self, answer_value):
		if self.current_round_text == "3-6-9":
			self.handle_369_answer_correct()

	def answer_pass(self):
		if self.current_round_text == "3-6-9":
			self.handle_369_answer_pass()

	# 
	# 3-6-9
	#

	def handle_369_answer_correct(self):
		# If this is the third question in 3-6-9, award 10 seconds
		if (self.current_subround + 1) % 3 == 0:
			self.active_player.points += 10

		# Then, move on to the next question
		self.advance_subround()

	def handle_369_answer_pass(self):
		self.add_current_player_to_turn_history()
		self.advance_turn_simply()