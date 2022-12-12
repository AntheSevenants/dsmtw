class Puzzel {
	static renderState(state) {
		let puzzle = document.getElementById("round_Puzzel_puzzle");
		if (state.turn_history.length == 1 && !state.timer_running && !host) {
			puzzle.style.visibility = "hidden";
		} else {
			puzzle.style.visibility = "visible";
		}

		// Puzzle matrix
		let answerColours = [ "teal", "yellow", "green" ];

		for (let i = 0; i < state.current_question.keywords.length; i++) {
			let keyword = state.current_question.keywords[i];
			let answerIndex = state.current_question.answer_indices[i];

			let keywordElement = document.getElementById(`round_Puzzel_puzzle_keyword_${i}`);
			keywordElement.innerHTML = keyword;
			keywordElement.className = "";

			if (state.answers_found.includes(answerIndex)) {
				keywordElement.classList.add(answerColours[answerIndex]);
			}
		}
	}
}