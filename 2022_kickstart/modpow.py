def modpow(base, pow, mod):
    """
        gives modulo power of base
        Even number of powering can be splited into lesser computing step
    """
    # basecase
    if pow == 0:
        return 1 % mod
    if pow == 1:
        return base % mod
    
    # else, 
    res = modpow((base*base)%mod, pow/2, mod)
    if (pow%2==1):
        return (base*res)%mod
    return res

def ebs(x, n):
    # x^n, exp_by_squaring
    if n==0:
        return 1
    elif n%2==1:
        # odd power
        return ebs(x*x, n/2)
    elif n%2==0:
        # even power
        return x*ebs(x*x, (n-1)/2)
    