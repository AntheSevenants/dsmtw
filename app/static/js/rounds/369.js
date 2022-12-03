class ThreeSixNine {
	static renderState(state) {
		console.log("miep");

		// Get all question circles
		let circles = Array.from(document.querySelectorAll(".ThreeSixNine.circle"));

		console.log(circles);

		circles.forEach(circle => {
			circle.classList.remove("turn");

			if (state.current_subround + 1 == circle.getAttribute("dsmtw-question-number")) {
				circle.classList.add("turn");
			}
		});
	}
}