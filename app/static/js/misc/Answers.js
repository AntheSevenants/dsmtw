class Answers {
	static renderAnswers(state) {
		if (state.current_question == null) {
			return;
		}

		if (!("answers" in state.current_question)) {
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

				// Dyanmic scoring for Collectief geheugen round
				if (state.current_round_text == "Collectief geheugen") {
					// We get the index of this answer in the found answers
					let foundIndex = state.answers_found.indexOf(i);
					answerScoreElement.innerHTML = state.awarded_seconds[foundIndex];
				}
			} else {
				answerTextElement.onclick = () => {
					dsmtw.correct(i);
				};
			}
		}
	}
}