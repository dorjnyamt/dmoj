line = input()

honi = ""
lastchar = ""
number = 0
for char in line:
    if char == "H" and lastchar == "":
        honi = honi + char
        lastchar = 'H'
    elif char == "O" and lastchar == "H":
        honi = honi + char
        lastchar = 'O'
    elif char == "N" and lastchar == "O":
        honi = honi + char
        lastchar = 'N'
    elif char == "I" and lastchar == "N":
        honi = honi + char
        lastchar = 'I'
        
    if honi == "HONI":
        number = number + 1
        honi = ""
        lastchar = ""

print(number)
