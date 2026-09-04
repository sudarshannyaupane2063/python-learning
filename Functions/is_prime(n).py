# To find given number is prime or not

def is_prime(n):
    if n<=1:
        return False

    i = 2
    while i<n:
        if n%i==0:
            return False
        i+=1

    return True

print(is_prime(int(input("Enter number to check prime:"))))