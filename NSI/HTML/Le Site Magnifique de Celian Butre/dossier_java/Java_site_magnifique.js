function mettreRouge() {
    document.querySelector("#optRed").style.color="red";
} // met en rouge une ligne de text
function foncEntre(){
	document.querySelector("#maDiv").classList.remove("blanc");
	document.querySelector("#maDiv").classList.add("rouge");
}
function foncQuitte() {
	document.querySelector("#maDiv").classList.remove("rouge");
	document.querySelector("#maDiv").classList.add("blanc");
}
			
