/// PART 8 - LOOP EXERCISES
// Before we continue on with your project, let's practice some loops!
// You'll have just two problems, but you'll need to use each loop type we
// learned about to solve them!


///////////////////
//// PROBLEM 1 ///
/////////////////

// Use a For Loop to print (console.log()) out the word "hello" 5 times.
//
// Do this with a While Loop and a For Loop

// While Loop
for (i = 0; i < 5; i++) {
    console.log("Hello")
}


// For Loop
var count = 5
while (count != 0) {
    console.log("Hello")
    count = count - 1
}



/////////////////
// PROBLEM 2 ///
///////////////

// Use Loops to console.log() (print out) all the odd numbers from 1 to 25
// Do this using two methods, a while loop and a for loop

// METHOD ONE
// While Loop
count = 0
while (count <= 25) {
    if (count % 2 != 0) {
        console.log(count)
    }
    count = count + 1
}

// METHOD TWO
// For Loop
for (i = 1; i <= 25; i++) {
    if (i % 2 != 0) {
        console.log(i)
    }
}
