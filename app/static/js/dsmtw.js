class DeSlimsteMens extends Gameshow {
	constructor() {
		super();

		this._currentSubroundText = null;

		this.scoreDomBuilt = false;
	}

	renderState(state) {
		if (!this.scoreDomBuilt) {
			this.buildScoreDom(state);
		}

		super.renderState(state);

		document.getElementById("currentround").innerHTML = state.current_round_text;

		if (host)
		{
			this.renderStateHost(state);
		}
		else
		{
			this.renderStateGame(state);
		}
	}

	renderStateHost(state) {

	}

	renderStateGame(state) {

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

	getCircleElementName(playerIndex) {
		return `circle_player_${playerIndex}`;
	}

	getScoreElementName(playerIndex) {
		return `score_player_${playerIndex}`;
	}
}

dsmtw = new DeSlimsteMens();