class Timer {
	constructor(scores, activePlayerIndex, startingPoints) {
		//this.startTime = this.getEpoch();

		this.scores = scores;
		this.activePlayerIndex = activePlayerIndex;
		this.currentPoints = startingPoints;

		// Parent can check whether the timer isr unning
		this.running = false;

		this.interval = null;
	}

	start() {
		this.interval = setInterval(() => { this.tick(); }, 1000);
		this.running = true;
	}

	stop() {
		if (this.interval != null) {
			clearInterval(this.interval);
		}
		this.running = false;
	}

	tick() {
		this.currentPoints -= 1;
		this.scores.adjustPlayerPoints(this.activePlayerIndex, this.currentPoints);
	}

	getEpoch() {
		return new Date().getTime() / 1000;
	}
}