class Galerij {
	static renderState(state) {
		let slideshowControl = document.getElementById("round_Galerij_slideshow_controls");
		slideshowControl.classList.remove("d-none");
		let answersElement = document.getElementById("round_Galerij_answers");
		answersElement.classList.remove("d-none");

		if (state.turn_history.length > 1) {
			slideshowControl.classList.add("d-none");
		} else {
			answersElement.classList.add("d-none");
		}

		if (host) {
			document.getElementById("round_Galerij_answer").innerHTML = 
				state.current_question.answers[state.galerij_index];

			document.getElementById("round_Galerij_correct_button").onclick = () => {
				dsmtw.correct(state.galerij_index);
			};
		}

	}
}