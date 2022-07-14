def multiply(x):
    
    def secmultiply(n):
        
        return x * n 

    return secmultiply


TimesTen = multiply(10)
TimesTwenty = multiply(20)

print (TimesTen(2)) #It prints 20
print (TimesTwenty(2))  # Prints 40
