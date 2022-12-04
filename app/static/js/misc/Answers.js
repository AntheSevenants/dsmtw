class Answers {
	static renderAnswers(state) {
		if (state.current_question == null) {
			return;
		}

		for (let i = 0; i < state.current_question.answers.length; i++) {
			let answer = state.current_question.answers[i];
			let currentRound = state.current_round_text;

			let answerTextElement = document.getElementById(`round_${currentRound}_answer_${i}`);
			answerTextElement.innerHTML = answer;
			answerTextElement.classList.remove("found");

			let answerScoreElement = document.getElementById(`round_${currentRound}_answer_score_${i}`);
			answerScoreElement.classList.remove("found");

			if (state.answers_found.includes(i)) {
				answerTextElement.classList.add("found");
				answerScoreElement.classList.add("found");
			} else {
				answerTextElement.onclick = () => {
					dsmtw.correct(i);
				};
			}
		}
	}
}