# Enigma Machine Simulator

Simple Enigma Machine Simulator without the plugboard. Meant as a beginner JS project.

<a title="MesserWoland, CC BY-SA 3.0 &lt;http://creativecommons.org/licenses/by-sa/3.0/&gt;, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Enigma_wiring_kleur.svg"><img width="256" alt="Enigma Machine wiring schema" src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Enigma_wiring_kleur.svg/256px-Enigma_wiring_kleur.svg.png?20150307085423"></a>

[Animation of the enigma machine by Jared Owen](https://www.youtube.com/watch?v=ybkkiGtJmkM)

Materials on writing JS code:
- [MDN Curriculum](https://developer.mozilla.org/en-US/curriculum/core/javascript-fundamentals/)
- [JavaScript in Y minutes](https://learnxinyminutes.com/docs/javascript/)
- [W3 Schools](https://www.w3schools.com/js/)

## Tasks

1. Retrieve the rotor data from the HTML using getElementById. Make sure these are numbers. Assign them to variables and log them to the console.
2. Using `search` and `slice`/`array[index]`, find the index of the rotor data in the `alphabet` string and retrieve the corresponding letter from the `rotor1_translations` string. Log this to the console.
3. Implement this as a function that takes the rotor data, and the letter as arguments and returns the translated letter.
4. Implement the reverse pass using an additonal function parameter and an if statement.
5. Use it to create a function that translates a letter through all the rotors and back.
6. Using a loop, implement a function that translates a string through the rotors. Try implementing it with a `for` loop, `apply` loop, and a `forEach` loop. If you're feeling adventurous, try implementing it with a `while` loop. Doing these might award you extra points ;)
7. Make sure the rotors move after each letter is translated. Rotor 2 and 3 should only move once per previous rotor's cycle.
8. Retrieve the input string from the HTML, pass it through the rotors and write the output to the HTML.
9. Ensure that the input string is converted to uppercase before being passed through the rotors.
10. Connect the code to the button. Make sure rotor values are modified after the button is clicked.

## Bonus content!
11. Implement a plugboard. Using `fetch` retrieve the current plugboard from `plugboard.json` and use it to translate the input string at the beginning and reverse translate it at the end.
12. Try refactoring the code to use classes.