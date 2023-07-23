# Treasure Map

row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
board = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

location = input("Location: ")
x = int(location[0]) % 3
y = int(location[1]) % 3

board[x][y] = "X"

print(f"{row1}\n{row2}\n{row3}")