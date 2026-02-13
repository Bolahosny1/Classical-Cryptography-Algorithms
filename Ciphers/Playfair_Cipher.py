msg = input("Enter the message: ").upper().replace("J", "I").replace(" ", "")
key = input("Enter the keyword: ").upper().replace("J", "I")
mode = input("Type E to Encrypt or D to Decrypt: ").upper()


letters = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
seen = []
for ch in key + letters:
    if ch not in seen:
        seen.append(ch)


grid = [seen[i:i+5] for i in range(0, 25, 5)]

# Display Table
print("\nPlayfair Table:")
for row in grid:
    print(" ".join(row))



pairs = []
i = 0

while i < len(msg):
    a = msg[i]

    if i + 1 < len(msg):
        b = msg[i+1]
        if a == b:
            pairs.append(a + "X")
            i += 1
        else:
            pairs.append(a + b)
            i += 2
    else:
        pairs.append(a + "X")
        i += 1

print("\nPairs:", pairs)



def locate(ch):
    for r in range(5):
        if ch in grid[r]:
            return r, grid[r].index(ch)
    return None, None



output = ""

for pair in pairs:
    a, b = pair[0], pair[1]
    r1, c1 = locate(a)
    r2, c2 = locate(b)

    if r1 == r2:
        if mode == "E":
            output += grid[r1][(c1 + 1) % 5]
            output += grid[r2][(c2 + 1) % 5]
        else:
            output += grid[r1][(c1 - 1) % 5]
            output += grid[r2][(c2 - 1) % 5]


    elif c1 == c2:
        if mode == "E":
            output += grid[(r1 + 1) % 5][c1]
            output += grid[(r2 + 1) % 5][c2]
        else:
            output += grid[(r1 - 1) % 5][c1]
            output += grid[(r2 - 1) % 5][c2]


    else:
        output += grid[r1][c2]
        output += grid[r2][c1]

print("\nResult:", output)
