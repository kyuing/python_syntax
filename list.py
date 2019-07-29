#container: list
square = [1, 'four', 9, 16, 25]
print(square)

#indexing
print(square[0])
print(square[1])
print(square[2])
print(square[3])
print(square[4])

#length
print(len(square))

#assign a new value into an index
square[1] = 4
print(square)

#delete an element by index
del square[3]
print(square)

#append an item to the right
square.append('kyu')
print(square)
