class Sound {
	static playSound(soundName) {
		Sound.playStopSound(soundName, true);
	}

	static stopSound(soundName) {
		Sound.playStopSound(soundName, false);
	}

	static playStopSound(soundName, play) {
		let soundElement = document.getElementById(`snd_${soundName}`);

		if (play) {
			soundElement.currentTime = 0;
			soundElement.play();
		} else {
			soundElement.stop();
		}
	}
}