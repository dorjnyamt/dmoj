button = 0
playlist = 'ABCDE'

while button != 4:
    button = int(input())
    times = int(input())
    while times > 0:
        if button == 1:
            playlist = playlist[1:5] + playlist[0]
        elif button == 2:
            playlist = playlist[4] + playlist[0:4]
        elif button == 3:
            playlist = playlist[1] + playlist[0] + playlist[2:5]

        times = times - 1

print(f"{playlist[0]} {playlist[1]} {playlist[2]} {playlist[3]} {playlist[4]}")
