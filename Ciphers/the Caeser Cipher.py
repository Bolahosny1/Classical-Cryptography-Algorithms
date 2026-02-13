
word = input("Enter your text: ")
key = int(input("Enter key number: "))


cipher_text = ""
for letter in word:
    if letter.isalpha():
        shifted = ord(letter) + key
        if letter.islower():
            if shifted > ord('z'):
                shifted -= 26
        elif letter.isupper():
            if shifted > ord('Z'):
                shifted -= 26
        cipher_text += chr(shifted)
    else:
        cipher_text += letter

print("Encrypted:", cipher_text)


plain_text = ""
for letter in cipher_text:
    if letter.isalpha():
        shifted = ord(letter) - key
        if letter.islower():
            if shifted < ord('a'):
                shifted += 26
        elif letter.isupper():
            if shifted < ord('A'):
                shifted += 26
        plain_text += chr(shifted)
    else:
        plain_text += letter

print("Decrypted:", plain_text)
