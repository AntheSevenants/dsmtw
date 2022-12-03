import json
import os.path

from gameshow.gameshow import Gameshow

class DeSlimsteMens(Gameshow):
	def __init__(self, no_players):
		rounds = [ "3-6-9", "Open deur", "Puzzel", "Galerij", "Collectief geheugen",
				   "Finale" ]

		super().__init__("De Slimste Mens Ter Wereld", rounds, no_players)