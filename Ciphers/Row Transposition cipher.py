msg = input("Enter the message: ").replace(" ", "").lower()
key = input("Enter the numeric key (e.g. 3142): ")

order = sorted(list(key))

cols = len(key)

while len(msg) % cols != 0:
    msg += "x"

matrix = []
idx = 0
for _ in range(len(msg) // cols):
    matrix.append(list(msg[idx:idx+cols]))
    idx += cols

cipher = ""
for char in order:
    col_index = key.index(char)
    for r in matrix:
        cipher += r[col_index]

print("\nEncrypted Text:", cipher)

rows = len(cipher) // cols
table = [["" for c in range(cols)] for r in range(rows)]

ci = 0
for char in order:
    col_index = key.index(char)
    for r in range(rows):
        table[r][col_index] = cipher[ci]
        ci += 1

plain = "".join("".join(r) for r in table)
plain = plain.rstrip("x")

print("Decrypted Text:", plain)
