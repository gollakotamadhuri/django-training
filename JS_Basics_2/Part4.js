useroptn = prompt("Would you like to start the web app? Type y for yes")
arr = []
while (useroptn == 'y') {
    command = prompt("Welcome to the web app! The commands available are : add, remove, display, quit. Please select your command ")
    if (command == 'quit') {
        break
    }
    else if (command == 'add') {
        ele = prompt("PLease enter the name you want to add")
        arr.push(ele)
    }
    else if (command == 'remove') {
        ele = prompt("PLease enter the name you want to remove")
        arr.splice(arr.indexOf(ele), 1)

    }
    else {
        console.log(arr)
    }

}
