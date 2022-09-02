n = int(input())

s = 0
t = 0

for i in range(n):
    line = input()
    s = s + (line.count("S") + line.count("s"))
    t = t + (line.count("T") + line.count("t"))

if s >= t:
    print("French")
else:
    print("English")