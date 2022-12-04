import json
import os.path
import json

from gameshow.gameshow import Gameshow

class DeSlimsteMens(Gameshow):
	def __init__(self, players, questions_directory):
		rounds = [ "3-6-9", "Open deur", "Puzzel", "Galerij", "Collectief geheugen",
				   "Finale" ]

		no_players = len(players)

		super().__init__("De Slimste Mens Ter Wereld", rounds, no_players)

		self.settings = { "369_round_no": 15 }

		self.questions = [ [] for round_text in rounds ]

		for i, round_text in enumerate(self.rounds):
			questions_json_path = os.path.join(questions_directory, f"{round_text}.json")
			if os.path.exists(questions_json_path):
				with open(questions_json_path, "rt") as reader:
					self.questions[i] = json.loads(reader.read())
			else:
				print(f"Questions for round {round_text} not found!")

		self.set_current_question(0)
		self.available_questions = []

		self.answer_time = False

		self.set_active_player(0)
		self.reset_turn_history()

		for i, player in enumerate(players):
			self.players[i].name = player
			self.players[i].points = 60

	# 
	# Turn taking
	# 

	# We use the turn history to keep track of which players have already had a guess
	# in this specific subround. This allows game-crucial mechanics such as keeping track
	# of who can complement an answer first
	def reset_turn_history(self):
		self.turn_history = []

	# Add the index of the current player to the turn history
	def add_current_player_to_turn_history(self):
		self.turn_history.append(self.active_player_index)

	# Which answers have already been found?
	# Saves the indices!
	def reset_answers_found(self):
		self.answers_found = []

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

	def advance_turn_logically(self, history=None):
		if history is None:
			history = self.turn_history

		current_lowest_score = float('inf')
		next_player_index = None
		for player_index, player in enumerate(self.players):
			if player.points < current_lowest_score and player_index not in history:
				current_lowest_score = player.points
				next_player_index = player_index

		self.set_active_player(next_player_index)
		history.append(next_player_index)

	# 
	# Round flow
	# 

	# Advance round
	def advance_round(self):
		super().advance_round()

		self.reset_answers_found()

		if self.current_round_text in [ "3-6-9" ]:
			self.set_current_question(0)
		# Open deur does not have a rigid question structure
		# This makes my life much more difficult. Oh well
		elif self.current_round_text == "Open deur":
			self.player_history = []

			# Player with least seconds can start
			# Advance GLOBAL turn (= turn for who gets a questioneer)
			self.advance_turn_logically(history=self.player_history)
			# Advance INTERNAL turn (= turn for who gets to answer the questioneer question)
			# Will default to the same player as the GLOBAL turn
			self.advance_turn_logically()
			# Broadcast the available questioneers
			self.set_available_questions()

	# Advance the subround, and clear the turn history
	def advance_subround(self):
		if self.current_round_text == "3-6-9":
			if self.current_subround == self.settings["369_round_no"] - 1:
				self.advance_round()
		elif self.current_round_text == "Open deur":
			if self.current_subround == self.no_players - 1:
				self.advance_round()

			# We have to reset the current question, else the questioneer face will
			# remain visible on the screen
			self.current_question = None

			# We advance the turn within the *player* history, not within the *turn* history
			self.advance_turn_logically(history=self.player_history)

		super().advance_subround()

		# If answer time is True, the question has been asked 
		#and answering is allowed
		self.answer_time = False
		self.reset_answers_found()

		# Does NOT apply to Open deur, because the question order is free for this round
		if self.current_round_text != "Open deur":
			# Set the current question corresponding to the current subround!
			self.set_current_question(self.current_subround)
		
		self.reset_turn_history()

	def set_current_question(self, question_no):
		self.current_question = self.questions[self.current_round][question_no]

	def set_available_questions(self):
		self.available_questions = self.questions[self.current_round]
		self.question_history = []

	# 
	# Clock
	#

	def clock_start(self):
		pass

	def clock_stop(self):
		pass

	#
	# Answering
	# 

	def answer_correct(self, answer_value):
		if self.current_round_text == "3-6-9":
			self.handle_369_answer_correct()
		elif self.current_round_text == "Open deur":
			self.handle_open_deur_answer_correct(answer_value)

	def answer_pass(self):
		if self.current_round_text == "3-6-9":
			self.handle_369_answer_pass()
		elif self.current_round_text == "Open deur":
			self.handle_open_deur_answer_pass()

	def award_seconds(self, seconds):
		self.active_player.points += seconds

	# 
	# 3-6-9
	#

	def handle_369_answer_correct(self):
		# If this is the third question in 3-6-9, award 10 seconds
		if (self.current_subround + 1) % 3 == 0:
			self.award_seconds(10)

		# Then, move on to the next question
		self.advance_subround()

	def handle_369_answer_pass(self):
		self.add_current_player_to_turn_history()
		self.advance_turn_simply()


	# 
	# Open deur
	#

	def open_deur_choose(self, questioneer_index):
		if questioneer_index in self.question_history:
			print("Could not choose Open deur question; question was already asked")
			return False

		self.set_current_question(questioneer_index)
		self.question_history.append(questioneer_index)
		self.answer_time = True

		return self.current_question["video"]

	def handle_open_deur_answer_correct(self, answer_index):
		if answer_index in self.answers_found:
			print("Could not register answer; answer already found")
			return False

		# Add answer to found answer list
		self.answers_found.append(answer_index)
		self.award_seconds(20)

		if len(self.answers_found) == 4:
			self.clock_stop()

	def handle_open_deur_answer_pass(self):
		print("Turn history", self.turn_history)

		# If no one is left to guess, move on to the next questioneer choice
		if len(self.turn_history) == self.no_players:
			print("Player count", self.no_players)

			self.advance_subround()
			return

		self.advance_turn_logically()