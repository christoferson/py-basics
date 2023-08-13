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

def ceasar(plain_text : str, shift_amount : int):
    cipher_text = ""
    for letter in plain_text:
        letter_encoded = chr(ord(letter) + shift_amount)
        cipher_text += letter_encoded
    return cipher_text

def ceasar_v2(plain_text : str, shift_amount : int):
    cipher_text = ""
    for letter in plain_text:
        if " " == letter or letter.isnumeric():
            cipher_text += letter
            continue
        letter_encoded = chr(ord(letter) + shift_amount)
        cipher_text += letter_encoded
    return cipher_text

def process():

    cmd = input("Type encode to encode, decode to decode: ")

    cmd_elements = cmd.split(" ")
    if len(cmd_elements) != 3:
        print("Command Syntax invalid. encode|decode text.")
        return

    op = cmd.split(" ")[0].lower()
    text = cmd.split(" ")[1]
    shift = int(cmd.split(" ")[2]) % 23

    if "encode" == op:
        cipher_text = ceasar_v2(text, shift)
        print(f"Cipher: {cipher_text}") 
    else:
        plain_text = ceasar_v2(text, -shift)
        print(f"Plain:  {plain_text}") 

def process_main():
    continue_flag = True
    while continue_flag:
        process()
        continue_reply = input("Type yes to repeat: ")
        if continue_reply.lower() != "yes":
            continue_flag = False
            print("Goodbye")

if __name__ == "__main__":
    print("A")
    process_main()
