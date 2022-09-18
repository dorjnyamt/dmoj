# FIXME: Implement this.
height, width = map(int, input().split())
picture = [[0 for w in range(width)] for r in range(height)]
for i in range(height):
    row = input()
    for j in range(width):
        picture[i][j] = row[j]

rectangles = 0
for i in range(height):
    for j in range(width):
        corner = picture[i][j]
        if corner == "*":
            if picture[i][j - 1] == "." and picture[i - 1][j] == "." and i > 0 and j > 0:
                rectangles += 1
            elif (i == 0 and j == 0) or (i == 0 and j == width - 1) or (i == height - 1 and j == 0) or (i == height - 1 and j == width - 1):
                rectangles += 1
            else: 
                if height == 1 and j > 0:
                    rectangles += 1
                    if picture[i][j + 1] == "*":
                        rectangles -= 1

print(rectangles)