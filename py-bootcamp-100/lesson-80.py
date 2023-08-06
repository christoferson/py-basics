def encode(plain_text : str, shift_amount : int):
    cipher_text = ""
    for letter in plain_text:
        letter_encoded = chr(ord(letter) + shift_amount)
        cipher_text += letter_encoded
    return cipher_text

def decode(cipher_text : str, shift_amount : int):
    plaint_text = ""
    for letter in cipher_text:
        letter_decoded = chr(ord(letter) - shift_amount)
        plaint_text += letter_decoded
    return plaint_text

def main():

    cmd = input("Type encode to encode, decode to decode: ")

    cmd_elements = cmd.split(" ")
    if len(cmd_elements) != 2:
        print("Command Syntax invalid. encode|decode text.")
        return

    op = cmd.split(" ")[0].lower()
    text = cmd.split(" ")[1]

    if "encode" == op:
        cipher_text = encode(text, 2)
        print(f"Cipher: {cipher_text}") 
    else:
        plain_text = decode(text, 2)
        print(f"Plain:  {plain_text}") 


main()