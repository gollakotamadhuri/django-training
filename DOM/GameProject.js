var restartbtn = document.querySelector("#restart");
var tablecnt = document.querySelectorAll("td");

function restart() {
    for (i = 0; i < tablecnt.length; i++) {
        tablecnt[i].innerText = ""
    }
}

function tictac() {
    if (this.innerText == 'X') {
        this.innerText = "O"
    }
    else if (this.innerText == 'O') {
        this.innerText = ""
    }
    else {
        this.innerText = "X"
    }

}

for (i = 0; i < tablecnt.length; i++) {
    tablecnt[i].addEventListener('click', tictac)
}

restartbtn.addEventListener('click', restart)