msg = input("Enter message: ").replace(" ", "").lower()
rails = int(input("Enter number of rails: "))


zigzag = [[] for _ in range(rails)]

row = 0
step = 1

for ch in msg:
    zigzag[row].append(ch)

    if row == 0:
        step = 1
    elif row == rails - 1:
        step = -1

    row += step

cipher = "".join("".join(r) for r in zigzag)
print("\nEncrypted Text:", cipher)



pattern = [["?" for _ in msg] for _ in range(rails)]

row = 0
step = 1
for i in range(len(msg)):
    pattern[row][i] = "*"
    if row == 0:
        step = 1
    elif row == rails - 1:
        step = -1
    row += step


pos = 0
for r in range(rails):
    for c in range(len(msg)):
        if pattern[r][c] == "*":
            pattern[r][c] = cipher[pos]
            pos += 1

plain = ""
row = 0
step = 1
for i in range(len(msg)):
    plain += pattern[row][i]
    if row == 0:
        step = 1
    elif row == rails - 1:
        step = -1
    row += step

print("Decrypted Text:", plain)
