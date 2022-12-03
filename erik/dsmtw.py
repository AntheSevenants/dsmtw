import json
import os.path

from gameshow.gameshow import Gameshow

class DeSlimsteMens(Gameshow):
	def __init__(self, players):
		rounds = [ "3-6-9", "Open deur", "Puzzel", "Galerij", "Collectief geheugen",
				   "Finale" ]

		no_players = len(players)

		super().__init__("De Slimste Mens Ter Wereld", rounds, no_players)

		for i, player in enumerate(players):
			self.players[i].name = player