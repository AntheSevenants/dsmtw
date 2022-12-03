class DeSlimsteMens extends Gameshow {
	constructor() {
		super();

		this._currentSubroundText = null;
	}

	renderState(state) {
		super.renderState(state);

		document.getElementById("currentround").innerHTML = state.current_round_text;

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

dsmtw = new DeSlimsteMens();