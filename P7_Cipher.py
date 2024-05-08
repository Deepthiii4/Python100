alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()

shift = int(input("Type the shift number:\n"))

def caesar(direction,text,shift):
    if direction == "encode":
        cipher_text=""
        for i in text:
            pos=alphabet.index(i)
            new_pos=pos+shift
            cipher_text+=alphabet[new_pos]
        print(cipher_text)
    
    else:
        cipher_text=""
        for i in text:
            pos=alphabet.index(i)
            new_pos=pos-shift
            cipher_text+=alphabet[new_pos]
        print(cipher_text)

caesar(direction,text,shift)

