def factorial(n):
    """Computes factorial of a number n"""
    fac = n
    if n != 0:
        while n > 1:
            fac = fac * (n-1)
            n -= 1
        return fac
    else:
        return 1
    
def exp_x_approx(x, n):
    """estimates exp(x) using a taylor series with n+1 terms"""
    s = 0
    for i in range(0, n+1):
        s = s + ((x**i)/factorial(i))
    print()
    print("The approximation of e^", x, "with", "n =", n, "is:")
    print(s)
    print()

def obtain_x():
    """obtains x value from user"""
    print("Input value of x:")
    x = int(input("> "))
    return x

def obtain_n():
    """obtains n value from user"""
    print("Input number of terms n (must be > 0):")
    n = int(input("> "))
    return n

def check_n(n):
    if int(n) <= 0:
        print("Not usuable n value")
        return None
        obtain_n()
    else:
        return n
        
def intro():
    print()
    print("=====================================")
    print("Approx. of exp(x) using Taylor series")
    print("=====================================")
    print()

intro()
x = obtain_x()
n = obtain_n()
check_n(n)
exp_x_approx(x, n)
print("=====================================")
print()
