class Bumper {
	static playBumper(text) {
		let bumperContainer = document.getElementById("bumper");
		let bumperText = document.getElementById("bumper_text");

		bumperContainer.className = "";

		bumperText.className = "animate__animated animate__fadeInLeft"
		bumperText.innerHTML = text;

		let bumperTime = 4000;

		setTimeout(() => {
			bumperText.className = "animate__animated animate__fadeOutRight"
		 }, bumperTime);
	
		setTimeout(() => {
			bumperContainer.className = "d-none";
		}, bumperTime + 1000);
	}
}