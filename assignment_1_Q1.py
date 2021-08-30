a = 0 #initialize First variable
b = 1 #initialize Second variable

#create Empty list:
ans_empty = []
#Use While loop
while (a < 50):

    # Append value in list ans_empty
    ans_empty.append(a) 
    
    c = a + b 
    # Update Value
    a = b
    b = c 

print(*ans_empty)

