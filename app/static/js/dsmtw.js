class DeSlimsteMens extends Gameshow {
	constructor() {
		super();

		this.currentSubroundText = null;
	}

	renderState(state) {
		super.renderState(state);

		this.currentSubroundText = state.current_subround_text;

		if (host)
		{
			this.renderStateHost(state);
		}
		else
		{
			this.renderStateGame(state);
		}
	}

	renderStateHost(state) {

	}

	renderStateGame(state) {
		
	}
}