class Sound {
	static playSound(soundName) {
		document.getElementById(`snd_${soundName}`).play();
	}
}