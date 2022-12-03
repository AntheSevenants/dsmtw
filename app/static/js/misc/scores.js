class Scores {
	constructor() {
		this.scoreDomBuilt = false;
	}

	// Create the DOM for the scores of the players
	// Cannot be hardcoded anymore, since here in the future, 
	// we have variable player counts
	buildScoreDom(state) {
		for (let i = 0; i < state.players.length; i++) {
			let player = state.players[i];

			let circleBox = document.createElement("div");
			circleBox.className = "circlebox";

			let playerName = document.createElement("div")
			playerName.className = "name";
			playerName.innerHTML = player.name;

			let innerCircle = document.createElement("div");
			innerCircle.className = "circle";
			innerCircle.id = this.getCircleElementName(i);

			let score = document.createElement("p");
			score.className = "score";
			score.id = this.getScoreElementName(i);

			let background = document.createElement("div");
			background.className = "background";

			circleBox.appendChild(playerName);
			circleBox.appendChild(innerCircle);
			innerCircle.appendChild(score);
			innerCircle.appendChild(background);

			document.getElementById("scores").appendChild(circleBox);
		}

		this.scoreDomBuilt = true;
	}

	renderState(state) {
		// We only build the score badges ONCE
		if (!this.scoreDomBuilt) {
			this.buildScoreDom(state);
		}

		
	}

	getCircleElementName(playerIndex) {
		return `circle_player_${playerIndex}`;
	}

	getScoreElementName(playerIndex) {
		return `score_player_${playerIndex}`;
	}
}