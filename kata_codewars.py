def find_even_index(arr):
    for i in range(len(arr)):
            if sum(arr[:i]) == sum(arr[i+1:]):
                return i

    return -1
    
    


def to_camel_case(text):
    l = [text[i].upper() if not i == 0 and text[i - 1] == '_' else text[i] for i in range(len(list(text)))]
    return''.join(l).replace('_','')


#text = 'the_stealth_warrior'
#print(to_camel_case(text))


def countBits(n):
    return '{0:b}'.format(n).count('1')

#print(countBits(1234))


def diamond(n):
    if n % 2 is 0 or n < 0:
        return None
    else:
        dia = []
        for i in [i for i in range(n+1) if i % 2 is not 0]:
            dia.append(str('*' * i) + "\n")


def is_prime(num):
    for j in range(2, int(num**0.5) +1):
        if num % j == 0:
            return False
    return False if num in (0, 1) else True




def make_readable(seconds):
    return "{:02d}:{:02d}:{:02d}".format(int(seconds/3600), int((seconds % 3600)/60), int((seconds % 3600) % 60))




def bouncingBall(h, bounce, window):
    # your code
    if h > 0  and bounce > 0 and bounce < 1 and window < h:
        count = 1
        while h >= window:
            h = h*bounce
            count += 1
        return count
    else:
        return -1

print(bouncingBall(3, 0.66, 1.5))