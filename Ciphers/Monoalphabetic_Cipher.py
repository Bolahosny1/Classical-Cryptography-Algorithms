alphabet = "abcdefghijklmnopqrstuvwxyz"

key = input("Enter 26-letter key: ").lower()
message = input("Enter your message: ").lower()


encrypt_dict = dict(zip(alphabet, key))
decrypt_dict = dict(zip(key, alphabet))


cipher = ""
for ch in message:
    if ch in encrypt_dict:
        cipher += encrypt_dict[ch]
    else:
        cipher += ch
print("Encrypted:", cipher)


plain = ""
for ch in cipher:
    if ch in decrypt_dict:
        plain += decrypt_dict[ch]
    else:
        plain += ch
print("Decrypted:", plain)



