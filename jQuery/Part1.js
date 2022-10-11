$('h1').click(function () {
    console.log("There was a click")
})

$('li').click(function () {
    console.log("Any li was called")
})

$('h1').click(function () {
    $(this).text("I was changed!")
})

$('input').eq(0).keypress(function () {
    console.log(event)
    if (event.which == 13) {
        $('h3').css({ 'color': 'blue' })
    }

})

$('h1').on('dblclick', function () {
    $('h1').text("Selecting with jQuery")
})

$('input').eq(1).on('click', function () {
    $('.container').fadeOut(400)
})