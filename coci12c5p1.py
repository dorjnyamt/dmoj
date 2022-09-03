# FIXME: partial correctness 

composition = input().split("|")
print(composition)

a_minor = 0
c_major = 0
for note in composition:
    if note[0] in "ADE":
        a_minor = a_minor + 1
    elif note[0] in "CFG":
        c_major = c_major + 1

if a_minor > c_major:
    print("A-mol")
elif a_minor < c_major:
    print("C-dur")
else:
    if composition[-1][0] in "A":
        print("A-mol")
    else:
        print("C-dur")