var playerA = prompt("Player One: Enter Your Name, you will be Blue")
var colorA = "Blue"
var playerB = prompt("Player Two: Enter Your Name, you will be Red")
var colorB = "Red"

var rows = $('tr')

var currentPlayer = playerA
var currentColor = colorA
var turn = 1

function changecolor() {
    var col = $(this).closest("td").index()
    for (i = 6; i > -1; i--) {
        if (rows.eq(i).find('td').eq(col).css('background-color') == 'rgb(128, 128, 128)') {
            rows.eq(i).find('td').eq(col).css('background-color', currentColor)
            if (turn == 1) {
                turn--
                currentPlayer = playerB
                currentColor = colorB
            }
            else {
                turn = 1
                currentPlayer = playerA
                currentColor = colorA
            }
            $('h4').text(currentPlayer + ": it is your turn, please pick a column to drop your " + currentColor + " chip.")
            break
        }
    }

}

$('h4').text(currentPlayer + ": it is your turn, please pick a column to drop your " + currentColor + " chip.")
$('td').on('click', changecolor)
