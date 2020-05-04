def eprimo(num):
    I = 1
    divisor = 0
    while I <= num:
        r = num % I
        if r == 0:
            divisor = divisor + 1
        I = I + 1
    
    if divisor == 2:
        return True
    else:
        return False

def maior_primo(K):
    while K > 0:
        if not eprimo(K):
            K = K - 1
        else:
            break

    return K