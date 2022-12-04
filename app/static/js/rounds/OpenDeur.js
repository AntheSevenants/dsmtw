class OpenDeur {
	static renderState(state) {
		let targetElement = document.getElementById("round_Open deur_questioneers");

		targetElement.innerHTML = "";

		for (let i = 0; i < state.no_players; i++) {
			console.log(i);

			let column = document.createElement("div");
			column.className = "col";

			let image = document.createElement("img");
			image.className = "questioneer";
			image.src = `resources/${state.available_questions[i].image}`;

			column.appendChild(image);
			targetElement.appendChild(column);
		}
	}
}