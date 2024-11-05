const rotor1_translations = "ZOJMGLEKYCHFDXBSUTPRQWVNIA";
const rotor2_translations = "DFUAVBOPTLXJSRGHYNMICEZKQW";
const rotor3_translations = "TJMGOQDRVBUXCZEYFHWAKISLPN";
const reflector_translations = "KELHBSQDZOACURJWGNFXMYPTVI";

const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

var rotor1_input = document.getElementById("rotor1")
var rotor2_input = document.getElementById("rotor2")
var rotor3_input = document.getElementById("rotor3")

function translate_letter_through_rotor(to_encode, rotor_translation, rotor_position, reversed) {
    if (reversed) {
        var index = (rotor_translation.search(to_encode) + 27 - rotor_position) % 26
        return alphabet[index]
    } else {
        var index = (alphabet.search(to_encode) + rotor_position - 1) % 26
        return rotor_translation[index]   
    }
}

function translate_letter_through_all_rotors(letter, rotor1_pos, rotor2_pos, rotor3_pos) {
    // First rotor, forward pass
    var encoded = translate_letter_through_rotor(letter, rotor1_translations, rotor1_pos, false)
    // Second rotor, forward pass
    encoded = translate_letter_through_rotor(encoded, rotor2_translations, rotor2_pos, false)
    // Third rotor, forward pass
    encoded = translate_letter_through_rotor(encoded, rotor3_translations, rotor3_pos, false)

    // Reflector
    encoded = translate_letter_through_rotor(encoded, reflector_translations, 1, false)

    // Third rotor, backward pass
    encoded = translate_letter_through_rotor(encoded, rotor3_translations, rotor3_pos, true)
    // Second rotor, backward pass
    encoded = translate_letter_through_rotor(encoded, rotor2_translations, rotor2_pos, true)
    // First rotor, backward pass
    encoded = translate_letter_through_rotor(encoded, rotor1_translations, rotor1_pos, true)

    return encoded
}

function translate_text(text) {
    text = text.toUpperCase()

    var rotor1_value = Number(rotor1_input.value)
    var rotor2_value = Number(rotor2_input.value)
    var rotor3_value = Number(rotor3_input.value)

    var outgoing_text = ""
    for (let index = 0; index < text.length; index++) {
        const element = text[index];
        outgoing_text += translate_letter_through_all_rotors(element, rotor1_value, rotor2_value, rotor3_value)
        
        rotor1_value++
        if (rotor1_value > 26) {
            rotor1_value = rotor1_value - 26
            rotor2_value++
        }
        if (rotor2_value > 26) {
            rotor2_value = rotor2_value - 26
            rotor3_value = (rotor3_value + 1) % 26
        }
    }
    rotor1_input.value = rotor1_value
    rotor2_input.value = rotor2_value
    rotor3_input.value = rotor3_value
    return outgoing_text
}

var input_field = document.querySelector("#inputText")
var output_field = document.querySelectorAll("#outputText")[0]
var run_button = document.querySelector("button")

run_button.addEventListener(
    "click", () => {
        output_field.value = translate_text(input_field.value)
    }
)