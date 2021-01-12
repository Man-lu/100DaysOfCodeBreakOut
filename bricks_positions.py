positions =[]
x = -450
y = 120
for _ in range(5):
    for _ in range(19):
        positions.append((x, y))
        x += 50

        if x == 500:
            x = -450
            y += 40
#
# print(positions)
