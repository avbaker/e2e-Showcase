def zigzagconvert(s, rows):
    output = []
    for i in range(rows):
        output.append([])
    row = 0
    down = True
    for c in s:
        output[row].append(c)
        if down:
            if row + 1 > rows - 1:
                down = False
                row += -1
            else:
                row += 1
        else:
            if row - 1 < 0:
                down = True
                row += 1
            else:
                row += -1
    out = ""
    for line in output:
        thisstring = ""
        for thischar in line:
            thisstring = thisstring + thischar

        out = out + thisstring
    return out


print(zigzagconvert("This is a secret code", 5))