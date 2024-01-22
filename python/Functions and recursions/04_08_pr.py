#sum(n) = (n-1) +  n 
def recursive_sum(n):
    if n==0:
        return 0
    else:
        return n + recursive_sum(n-1)
    
number = 9
result = recursive_sum(number)
print(f"The sum of natural numbers up to {number} is: {result}")



