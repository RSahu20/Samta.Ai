""" Task 2: Generate Fibonacci Series """

# Fibonacci series up to n terms
def recur_fibo(n):  
    if n <= 1:  
        return n  
    else:  
        return(recur_fibo(n-1) + recur_fibo(n-2))  

# take input from the user  
number = int(input("Enter the number of terms: "))  

#  display Fibonacci sequence up to that number of terms
if number <= 0:  
    print("Please enter a positive integer")  
else:  
    print("Fibonacci sequence:", end=" ")  
    for i in range(number):  
        print(recur_fibo(i), end=" ") 

# time complexity == O(2^n)
# space complexity == O(n)