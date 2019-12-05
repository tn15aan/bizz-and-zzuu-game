print("Welcome to the bizzzzuu game")
num = int(input('Please choose a number: '))

def div_3(num):
    return num % 3 == 0

def div_5(num):
    return num % 5 == 0

def bizz_zzuu(num):
    if div_5(num) and div_3(num):
        return str(num) + ' is a multiple of 3 and 5, bizzzzuu'
    elif div_3(num):
        return str(num) + ' is a multiple of 3, bizz!'
    elif div_5(num):
        return str(num) + ' is a multiple of 5, zzuu!'
    else:
        return str(num) + ' is not a multiple of 3 or 5, please try again.'

def run(num):
    output = bizz_zzuu(num)
    return output
