def decode_message(encrypted_message):
    """
    Decode Mars rover encrypted message.
    
    Each character is shifted forward by its position (1-indexed).
    To decode, shift back by the position.
    
    """
    
    # Convert to uppercase
    encrypted_message = encrypted_message.upper()
    
    decoded = ""
    
    for position, char in enumerate(encrypted_message, start=1):
        # Get ASCII value of character
        char_code = ord(char)
        
        # Shift back by position
        # Handle wrapping (Z -> A wrapping)
        shifted_code = char_code - position
        
        # If we go below 'A', wrap around to end of alphabet
        while shifted_code < ord('A'):
            shifted_code += 26
        
        decoded += chr(shifted_code)
    
    return decoded
def main():
    """Main function to decode encrypted message."""
    # EACH WORD IS SHIFTED BACK BY ITS POS NO.
    
    encrypted = input("Enter encrypted message: ")
    decoded = decode_message(encrypted)
    
    print(f"\nEncrypted: {encrypted.upper()}")
    print(f"Decoded:   {decoded}\n")
 
 
if __name__ == "__main__":
    main()