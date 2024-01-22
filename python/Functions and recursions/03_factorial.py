#n! = 1 * 2 * 3 * 4...*n
#n = 4
#product = 1
#for i in range(n):
 #   product = product * (i + 1)
#print(product)

#WRAPPED IT IN A FUNCTION

def factorail_iter(n):
    product = 1
    for i in range(n):
        product = product * (i + 1)
    return product

def factorail_recursive(n):
    if n==1 or n==0:
        return 1
    return n * factorail_recursive(n-1)
print(factorail_recursive(5))
 