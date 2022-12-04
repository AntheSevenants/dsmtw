class AuxiliaryMedia {
	static renderState(state) {
		let container = document.getElementById("container_auxiliaryMedia");
		container.classList.add("d-none");

		if (state.current_question == null) {
			return;
		}

		if (!("image" in state.current_question) && !("video" in state.current_question)) {
			return;
		}

		if (state.current_question.image != null | state.current_question.video != null) {
			container.classList.remove("d-none");
		}

		if (state.current_question.image != null) {
			document.getElementById("auxiliaryMedia").src = 
				`/resources/${state.current_question.image}`;
		}
	}
}