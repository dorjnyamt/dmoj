# FIXED: partial correctness 

composition = input()

a_minor = 0
c_major = 0
for note in range(len(composition)):
    prev = note - 1
    if note == 0 or composition[prev] == "|":
        if composition[note] in "ADE":
            a_minor += 1
        elif composition[note] in "CFG":
            c_major += 1

if a_minor > c_major:
    print("A-mol")
elif a_minor < c_major:
    print("C-dur")
else:
    if composition[-1] == "A":
        print("A-mol")
    elif composition[-1] == "C":
        print("C-dur")