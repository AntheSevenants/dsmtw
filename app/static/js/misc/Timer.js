class Timer {
	constructor(scores,activePlayerIndex, startingPoints) {
		//this.startTime = this.getEpoch();

		this.scores = scores;
		this.activePlayerIndex = activePlayerIndex;
		this.currentPoints = startingPoints;

		this.interval = null;
	}

	start() {
		this.interval = setInterval(() => { this.tick(); }, 1000);
	}

	stop() {
		clearInterval(this.interval);
	}

	tick() {
		this.currentPoints -= 1;
		this.scores.adjustPlayerPoints(this.activePlayerIndex, this.currentPoints);
	}

	getEpoch() {
		return new Date().getTime() / 1000;
	}
}