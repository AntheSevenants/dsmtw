class DeSlimsteMens extends Gameshow {
	constructor() {
		super();

		this.websocket.on('points_awarded', (pointsAwarded) => { 
			this.pointsAwarded(pointsAwarded); });
		this.websocket.on('clock_start', () => { 
			this.clockStarted(); });
		this.websocket.on('clock_stop', () => { 
			this.clockStopped(); });

		this._currentSubroundText = null;

		this.scoreDomBuilt = false;

		this.scores = new Scores();

		this.latestState = null;
	}

	renderState(state) {
		// First state render
		if (this.latestState == null) {
			this.latestState = state;

			// We need to make a timer so we can cancel it, basically
			this.setupTimer();

			// Timer could have started before we loaded the page!
			if (state.timer_running) {
				this.timer.start();
			}
		}

		// If the clock has been stopped server side (this is possible when all answers were found),
		// we need to stop our local clock
		if (!state.timer_running && this.timer.running) {
			this.clockStopped();
		}

		// Save the latest state
		this.latestState = state;

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

		document.body.classList.remove("unadvanced");
		// Add a specific class if to_advance is not null
		if (state.to_advance != null) {
			document.body.classList.add("unadvanced");
		}

		// Round-specific rendering
		switch (state.current_round_text) {
			case "3-6-9":
				ThreeSixNine.renderState(state);
				break;
			case "Open deur":
				OpenDeur.renderState(state);
				Answers.renderAnswers(state);
				break;
			case "Puzzel":
				Puzzel.renderState(state);
				Answers.renderAnswers(state);
				break;
			case "Galerij":
				Galerij.renderState(state);
				Answers.renderAnswers(state);
				break;
			case "Collectief geheugen":
				CollectiefGeheugen.renderState(state);
				Answers.renderAnswers(state);
				break;
			case "Finale":
				Finale.renderState(state);
				Answers.renderAnswers(state);
				break;
		}

		// Render scores
		// Don't do this if a timer is running -> unreliable!
		if (!this.timer.running) {
			this.scores.renderState(state);
		}

		// Toggle the clock button UI
		// "Start klok" and "Stop klok"
		this.setClockUI(state.timer_running);

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

	pointsAwarded(pointsAwarded) {
		this.timer.currentPoints += pointsAwarded;
	}

	setupTimer() {
		this.timer = new Timer(this.scores,
							   this.latestState.active_player_index,
							   this.latestState.active_player.points);
	}

	clockStart() {
		this.websocket.emit("clock_start");
	}

	clockStarted() {
		this.setupTimer();
		this.timer.start();
	}

	clockStop() {
		this.websocket.emit("clock_stop");
	}

	clockStopped() {
		this.timer.stop();
	}

	clockToggle() {
		this.websocket.emit("clock_toggle");
	}

	setClockUI(timer_running) {
		document.getElementById("button_clock_toggle").innerHTML = 
			timer_running ? "Stop klok" : "Start klok";
	}

	releaseAdvance() {
		this.websocket.emit("release_advance");
	}
}

dsmtw = new DeSlimsteMens();