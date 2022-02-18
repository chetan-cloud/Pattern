print("Welcome to pattern generator")
print()

#Asks for number and makes sure it works
size= int(input("Please enter the size of the pattern (an odd number between 7 and 15): "))
while size< 7 or size > 15 or size%2 == 0:
    print("Size should be an odd number between 7 and 15")
    size= int(input("Please enter the size of the pattern (an odd number between 7 and 15): "))
print()
p1 = size
#Makes pattern 1
print("Pattern 1 of size " + str(size))
for k in range(1, p1+1):
    print("<" * p1 + "*" * (k*2-1) + ">" * p1)
    p1-=1

#mirror pattern
print("Mirror image pattern of size "+ str(size))
space = size*2 - 2
for i in range(1, size):
    
        
    print("A" *i + " " * space + "A" * i)
    space -=2
print("A" * (size*2))
space = 2

for l in range(size-1, 0,  -1):
    print("A" * l + " " *space + "A" * l)
    space+= 2
print()
print("Bye")
