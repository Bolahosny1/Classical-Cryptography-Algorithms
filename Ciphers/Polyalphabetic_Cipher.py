alphabet = "abcdefghijklmnopqrstuvwxyz"

message = input("Enter your message: ").lower()
rules = input("Enter numbers separated by spaces (e.g. 3 -1 4): ").split()
rules = [int(x) for x in rules]

cipher = ""
r = 0
for ch in message:
    if ch.isalpha():
        pos = alphabet.index(ch)
        shift = rules[r]
        new_pos = (pos + shift) % 26
        cipher += alphabet[new_pos]
        r = (r + 1) % len(rules)
    else:
        cipher += ch

print("Encrypted:", cipher)

plain = ""
r = 0
for ch in cipher:
    if ch.isalpha():
        pos = alphabet.index(ch)
        shift = rules[r]
        new_pos = (pos - shift) % 26
        plain += alphabet[new_pos]
        r = (r + 1) % len(rules)
    else:
        plain += ch

print("Decrypted:", plain)
