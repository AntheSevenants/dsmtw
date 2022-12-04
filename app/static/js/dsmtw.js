class DeSlimsteMens extends Gameshow {
	constructor() {
		super();

		this._currentSubroundText = null;

		this.scoreDomBuilt = false;

		this.scores = new Scores();
	}

	renderState(state) {
		// Pass to super method
		super.renderState(state);

		// Debug
		document.getElementById("currentround").innerHTML = state.current_round_text;

		// Hide all rounds...
		let roundContainers = document.getElementsByClassName("round");
		Array.from(roundContainers).forEach(roundContainer => 
			roundContainer.classList.remove("current"));
		// ..then only show the current one
		document.getElementById(`round_${state.current_round_text}`).classList.add("current");

		// Round-specific rendering
		switch (state.current_round_text) {
			case "3-6-9":
				ThreeSixNine.renderState(state);
				break;
			case "Open deur":
				OpenDeur.renderState(state);
				break;
		}

		// Render scores
		this.scores.renderState(state);

		// Render auxiliary media (if necessary)
		AuxiliaryMedia.renderState(state);

		// Host/client-specific rendering
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

	/* Communication */
	correct(answerValue = null)
	{
		this.websocket.emit("answer_correct", answerValue);
	}

	pass()
	{
		this.websocket.emit("answer_pass");
	}

	openDeurChoose(questioneerIndex) {
		this.websocket.emit("open_deur_choose", questioneerIndex);
	}
}

dsmtw = new DeSlimsteMens();