
#!python
print("content-type: text/html; charset=utf-8\n")
a = 'hola python'
print(a)

#length
print(len(a))

#index
print(a[0])
print(a[1])

#the last index
print(a[-1])

#slice; starts with 0 index not including index 4
print(a[0:4])

#repeat
print((a + '\n') * 2)
