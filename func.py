#code are here
a=1
b=2
c=3
s=a+b+c
r=s/3
print(s)    #print a sum
print(r)    #print an average
            #But it can be tired if you need to code again and again.

#Insted, we can define (create) a function (method in java)
print("\n" + "Instead, we can define (create) a function (method in java)")
def average():
    a=1
    b=2
    c=3
    s=a+b+c
    r=s/3
    print("sum: ", s)
    print("average", r)

# we then call the function
average()
