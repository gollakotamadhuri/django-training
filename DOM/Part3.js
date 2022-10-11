var headOne = document.querySelector("#one")
var headTwo = document.querySelector("#two")
var headThree = document.querySelector("#three")

console.log(headOne)
console.log(headTwo)
console.log(headThree)

headOne.addEventListener('mouseover', function () {
    headOne.textContent = "Mouse currently over"
    headOne.style.color = "RED"
})
headOne.addEventListener('mouseout', function () {
    headOne.textContent = "Hover over me"
    headOne.style.color = "Black"
})

headTwo.addEventListener('click', function () {
    headTwo.textContent = "Clicked on"
    headTwo.style.color = "Blue"
})

headTwo.addEventListener('dblclick', function () {
    headTwo.textContent = "Click me!"
    headTwo.style.color = "Black"
})

headThree.addEventListener('dblclick', function () {
    headThree.textContent = "I was double clicked"
    headThree.style.color = "Green"
})

headThree.addEventListener('click', function () {
    headThree.textContent = "Double click me"
    headThree.style.color = "Black"
})