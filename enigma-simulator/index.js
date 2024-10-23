
const rotor1_translations = "HIMBNSVTDXRKPAZOLUEJQWFCGY";
const rotor2_translations = "WOZIEBAPNYGVHMCKRXLJFUDTSQ";
const rotor3_translations = "QTSZGVRPYDHLMEBUJIAXWKCOFN";
const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

// Tasks:
// 1. Retrieve the rotor data from the HTML using getElementById. Make sure these are numbers. Assign them to variables and log them to the console.
// 2. Using `search` and `slice`/`array[index]`, find the index of the rotor data in the `alphabet` string and retrieve the corresponding letter from the `rotor1_translations` string. Log this to the console.
// 3. Implement this as a function that takes the rotor data, and the letter as arguments and returns the translated letter.
// 4. Implement a function for a reverse pass through the rotor.
// 5. Use it to create a function that translates a letter through the rotors.
// 6. Using a loop, implement a function that translates a string through the rotors. Try implementing it with a `for` loop, `apply` loop, and a `forEach` loop. If you're feeling adventurous, try implementing it with a `while` loop. Doing these might award you extra points ;)
// 7. Make sure the rotors move after each letter is translated. The 
// 8. Retrieve the input string from the HTML, pass it through the rotors and write the output to the HTML.
// 9. Ensure that the input string is converted to uppercase before being passed through the rotors.
// 10. Connect the code to the button. Make sure rotor values are modified after the button is clicked.
// 11. Implement a plugboard. Using `fetch` retrieve the current plugboard from `plugboard.json` and use it to translate the input string at the beginning and reverse translate it at the end.
// 12. Try refactoring the code to use classes.