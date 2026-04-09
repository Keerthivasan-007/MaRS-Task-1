def morse_to_text(morse_code):
    """
    Convert Morse code to plain English text.

    Input: Morse code string
    - Dots (.) and dashes (-) represent letters/numbers
    - Single space separates letters
    - Double space (or ' / ') separates words
    
    Output: Decoded English tex
    """
    # Morse code to character mapping
    morse_dict = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3',
        '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
        '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?',
        '.----.': "'", '-.-.-.': ';', '-....-': '-', '-.-.-': '+',
        '-..-.': '/', '.-..-.': '"', '-·-·--': '@', '...---...': 'SOS'
    }
    
    # Replace word separator with a special marker
    morse_code = morse_code.replace(' / ', '  ')  # Convert word separator to double space
    
    # Split by double space to get words
    words = morse_code.split('  ')
    
    decoded_text = []
    
    for word in words:
        if word:  # If word is not empty
            # Split word by single space to get individual Morse letters
            morse_letters = word.split(' ')
            decoded_word = ''
            
            for morse_letter in morse_letters:
                if morse_letter in morse_dict:
                    decoded_word += morse_dict[morse_letter]
                elif morse_letter:  # If it's not empty but not in dict
                    decoded_word += '?'  # Unknown character
            
            if decoded_word:
                decoded_text.append(decoded_word)
    
    return ' '.join(decoded_text)


def main():
    """Main function to get Morse code input and decode it."""    
    print("Format: dots (.) and dashes (-) for letters")
    print("  Single space = letter separator")
    print("  Double space or ' / ' = word separator")    
    morse_input = input("Enter Morse code: ")
    decoded = morse_to_text(morse_input)
    
    print(f"\nDecoded message: {decoded}\n")


if __name__ == "__main__":
    main()
