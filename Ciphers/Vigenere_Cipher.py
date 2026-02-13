alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def repeat_key(message, key):
    cleaned = [c for c in message if c.isalpha()]
    return (key * ((len(cleaned) // len(key)) + 1))[:len(cleaned)]

def encrypt(message, key):
    key = repeat_key(message, key)
    result = ""
    j = 0

    for char in message:
        if char.isalpha():
            m = alphabet.index(char.upper())
            k = alphabet.index(key[j])
            result += alphabet[(m + k) % 26]
            j += 1
        else:
            result += char
    return result

def decrypt(cipher, key):
    key = repeat_key(cipher, key)
    result = ""
    j = 0

    for char in cipher:
        if char.isalpha():
            c = alphabet.index(char.upper())
            k = alphabet.index(key[j])
            result += alphabet[(c - k) % 26]
            j += 1
        else:
            result += char
    return result

msg = input("Enter message: ").upper()
key = input("Enter key: ").upper()
mode = input("Encrypt (E) or Decrypt (D)? ").upper()

if mode == "E":
    print("\nCiphertext:", encrypt(msg, key))
else:
    print("\nDecrypted:", decrypt(msg, key))
