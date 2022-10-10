var firstname = prompt("Welcome! What is your firstname?")
var lastname = prompt("What is your lastname?")
var age = prompt("What is your age?")
var height = prompt("What is your height in cms?")
var petname = prompt("What is the name of your pet?")

if ((firstname[0].toLowerCase() === lastname[0].toLowerCase()) && (age > 20 && age < 30) && (height > 170) && petname[petname.length - 1].toLowerCase() === "y") {
    console.log("Well, hello Sherlock!")
}
else {
    console.log("Nothing to see here!")
}