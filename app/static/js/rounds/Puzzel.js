class Puzzel {
	static renderState(state) {
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