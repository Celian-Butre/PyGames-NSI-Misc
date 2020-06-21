function tuOseMSG() {
	alert("Tu ose?!")
} // alert si quelqu'un essaie de dire que Célian Butré n'est pas ouf

alert("Attention, la censure est mis en place sur ce QCM")
// indique que la censure est mis en place à l'ouverture de la page

function WrongAnswer(){
	document.querySelector("#maDiv").classList.remove("vert");
	document.querySelector("#maDiv").classList.add("rouge");
}
function CorrectAnswer() {
	document.querySelector("#maDiv").classList.remove("rouge");
	document.querySelector("#maDiv").classList.add("vert");
}